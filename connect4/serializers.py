from .models import Audit
from rest_framework import serializers

class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model=Audit
        fields="__all__"