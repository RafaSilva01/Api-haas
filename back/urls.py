from django.urls import path, include
from rest_framework import routers
from .views import ItemConfigurcaoViewSet

router = routers.DefaultRouter()
router.register(r'itemConfiguracao', ItemConfigurcaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-alt/', include('rest_framework.urls', namespace = 'rest_framework'))
]