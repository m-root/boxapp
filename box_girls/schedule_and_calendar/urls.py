from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'activity', ActivityScheduleAndCalendarViewSet, base_name='api_activity')
urlpatterns = [] + router.urls