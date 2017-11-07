from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'activity', ActivityViewSet, base_name='api_activity')
urlpatterns = [] + router.urls