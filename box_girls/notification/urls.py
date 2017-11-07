from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'notification', NotificationViewSet, base_name='api_notification')
urlpatterns = [] + router.urls