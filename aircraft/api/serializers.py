from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from aircraft.models import Aircraft

class AircraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = [
            'id',
            'aircraft',
            'type',
            'status',
            'info_count',
            'errors_count'
        ]