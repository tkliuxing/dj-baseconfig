from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'baseconfigcategory', api.BaseConfigCategoryViewSet)
router.register(r'baseconfigcategorynamed', api.BaseConfigCategoryNamedViewSet)
router.register(r'baseconfigitem', api.BaseConfigItemViewSet)
router.register(r'baseconfigvalue', api.BaseConfigValueViewSet)
router.register(r'baseconfigfileupload', api.BaseConfigFileUploadViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)
