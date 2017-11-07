from django.conf import settings

from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response


from .serializers import *

class MembershipRegistrationViewSet(viewsets.ModelViewSet):
    queryset = MembershipRegistration.objects.all()
    serializer_class = MembershipRegistrationSerializer


class GuardianViewSet(viewsets.ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer