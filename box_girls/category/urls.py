from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, base_name='api_category')
urlpatterns = [] + router.urls