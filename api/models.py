from time import timezone

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Модель продукта.
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def has_access(self, user):
        return self.group_set.filter(students=user).exists()


class Lesson(models.Model):
    """
    Модель урока.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='lessons',
    )
    name = models.CharField(max_length=100)
    video_link = models.URLField()

    def __str__(self):
        return self.name


class Group(models.Model):
    """
    Модель группы.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    min_users = models.SmallIntegerField()
    max_user = models.SmallIntegerField()
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def distribute_users_to_groups(self, user):
        """
        Метод для распределения пользователей по группам продукта.
        """
        if self.product.start_date > timezone.now():
            groups = Group.objects.filter(product=self.product).order_by(
                'students__count', 'max_users'
            )

            if not groups:
                return 'There are no groups available for this product.'

            min_users = min(group.students.count() for group in groups)
            max_users = max(group.students.count() for group in groups)

            if max_users - min_users <= 1:
                target_group = min(
                    (
                        group for group in groups
                        if group.students.count() < group.max_users
                    ),
                    key=lambda group: (
                        group.students.count(), -group.max_users
                    ),
                )
                target_group.students.add(user)
                return f'User {user.username} added to group: {target_group.name}'
            else:
                return 'Groups have too much imbalance to distribute users.'
        else:
            return 'Product has already started. Cannot distribute users.'
