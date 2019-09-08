from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'baseconfigcategory', api.BaseConfigCategoryViewSet)
router.register(r'baseconfigitem', api.BaseConfigItemViewSet)
router.register(r'baseconfigvalue', api.BaseConfigValueViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/', include(router.urls)),
)
