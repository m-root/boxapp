from rest_framework import serializers

from .models import *

class MembershipRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipRegistration
        fields ='__all__'

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields ='__all__'
