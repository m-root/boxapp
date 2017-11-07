from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'', ViewSet, base_name='api_')

urlpatterns = [] + router.urls