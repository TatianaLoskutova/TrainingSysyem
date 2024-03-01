from rest_framework import serializers
from django.db.models import Count, F, ExpressionWrapper, FloatField

from .models import Product, Lesson, User


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор урока.
    """

    class Meta:
        model = Lesson
        fields = ('name', 'video_link')


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор продукта.
    """

    lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'start_date', 'price', 'lessons')


class ProductStatisticSerializer(serializers.ModelSerializer):
    """
    Сериализатор статистики по продукту.
    """

    total_students = serializers.SerializerMethodField()
    group_fill_percentage = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'name', 'total_students', 'group_fill_percentage',
            'purchase_percentage',
        )

    def get_total_students(self, obj):
        return obj.group_set.all().aggregate(
            total_students=Count('students')
        )['total_students']

    def get_group_fill_percentage(self, obj):
        avg_fill_percentage = obj.group_set.annotate(
            fill_percentage=ExpressionWrapper(
                (Count('students') * 100.0) / F('max_users'),
                output_field=FloatField(),
            )
        ).aggregate(
            avg_fill_percentage=Count('id', distinct=True)
        )['avg_fill_percentage']
        return avg_fill_percentage

    def get_purchase_percentage(self, obj):
        total_users = User.objects.count()
        access_count = obj.group_set.aggregate(
            total_access=Count('students')
        )['total_access']
        return (access_count / total_users) * 100 if total_users > 0 else 0
