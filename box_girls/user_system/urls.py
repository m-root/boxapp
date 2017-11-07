from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'membership_registration', MembershipRegistrationViewSet, base_name='api_membership_regustration')
router.register(r'guardian', GuardianViewSet, base_name='api_guardian')
urlpatterns = [] + router.urls