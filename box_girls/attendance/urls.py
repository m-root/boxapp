from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'attendance', AttendanceViewSet, base_name='api_attendance')
urlpatterns = [] + router.urls