from rest_framework.viewsets import ModelViewSet

from aircraft.models import Aircraft
from aircraft.api.serializers import AircraftSerializer

class AircraftViewset(ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer



