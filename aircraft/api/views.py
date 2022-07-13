
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import csv
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.core.serializers import serialize
from aircraft.api.utils.constants import KindStatus
from aircraft.models import Aircraft

@method_decorator(name='get', decorator=swagger_auto_schema(
    manual_parameters=[]
))
class DataView(APIView):

    q = """
        SELECT 
        COUNT(CASE WHEN b.type = 'Legend'  THEN 0 END) as legend,
        COUNT(CASE WHEN b.type = 'Lower A' THEN 0 END) as lower_a,
        COUNT(CASE WHEN b.type = 'Lower B' THEN 0 END) as lower_b,
        COUNT(CASE WHEN b.type = 'Warning' THEN 0 END) as warning,
        COUNT(CASE WHEN b.type = 'Paired B' THEN 0 END) as paired_b,
        COUNT(CASE WHEN b.type = 'Repeat Legend' THEN 0 END) as repeat_legend,
        COUNT(CASE WHEN b.type = 'Upper A' THEN 0 END) as upper_a,
        COUNT(CASE WHEN b.type = 'Paired A' THEN 0 END) as paired_a,
        COUNT(CASE WHEN b.type = 'PreLegend' THEN 0 END) as pre_legend,
        SUM(b.info_count) as info_count, 
        SUM(b.errors_count) as errors_count,
        b.aircraft aircraft,b.status status,b.type type,
        null as id
        FROM aircraft_aircraft B
        GROUP BY grouping sets( (b.aircraft),(b.status),(b.type))
        """
   
    def get(self, request):
       
        data=Aircraft.objects.raw(self.q)
        jdata=({
                'legend':x.legend,
                'lower_a':x.lower_a,
                'lower_b':x.lower_b,
                'warning':x.warning,
                'paired_b':x.paired_b,
                'repeat_legend':x.repeat_legend,
                'upper_a':x.upper_a,
                'paired_a':x.paired_a,
                'pre_legend':x.pre_legend,
                'info_count':x.info_count,
                'errors_count':x.errors_count,
                'aircraft':x.aircraft,
                'status':x.status,
                'type':x.type
                } for x in data)
        return Response(jdata,status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        with open('test_data.csv') as file:
            reader = csv.reader(file)

            for row in list(reader)[1:]:
                Aircraft.objects.create(
                    priority=row[0],
                    type = row[1],
                    aircraft = row[2],
                    status = row[3],
                    errors_count = row[4],
                    info_count = row[5],
                )
        return Response(status=status.HTTP_201_CREATED)

    