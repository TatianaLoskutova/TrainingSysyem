from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from api.views import ProductViewSet, ProductStatisticViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(
    r'statistic', ProductStatisticViewSet, basename='productstatistic',
)

urlpatterns = [
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
    )
