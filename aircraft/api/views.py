
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
        SUM(query1.info_count) info_count,
        SUM(query1.error_count) error_count,
        query1.aircraft as name ,
        SUM(query1.legend) legend,
        SUM(query1.lower_a) lower_a,
        SUM(query1.lower_b) lower_b,
        SUM(query1.paired_a) paired_a,
        SUM(query1.paired_b) paired_b,
        SUM(query1.pre_legend) pre_legend,
        SUM(query1.repeat_legend) repeat_legend,
        SUM(query1.upper_a) upper_a,
        SUM(query1.warning) warning,
        query1.aircraft,
        null as type,
        null as status,
        null as id
        FROM 
        (SELECT  DISTINCT(b.aircraft), COUNT(b.type) AS count_type,b.type,
        SUM(b.info_count) as info_count, 
        SUM(b.errors_count) as error_count,
        CASE
            WHEN b.type = 'Legend' THEN count(b.type) ELSE 0
        END AS legend,
        CASE
            WHEN b.type = 'Lower A' THEN count(b.type) ELSE 0
        END AS lower_a,
        CASE
            WHEN b.type = 'Lower B' THEN count(b.type) ELSE 0
        END AS lower_b,
        CASE
            WHEN b.type = 'Paired A' THEN count(b.type) ELSE 0
        END AS paired_a,
        CASE
            WHEN b.type = 'Paired B' THEN count(b.type) ELSE 0
        END AS paired_b,
        CASE
            WHEN b.type = 'PreLegend' THEN count(b.type) ELSE 0
        END AS pre_legend,
        CASE
            WHEN b.type = 'Repeat Legend' THEN count(b.type) ELSE 0
        END AS repeat_legend,
        CASE
            WHEN b.type = 'Upper A' THEN count(b.type) ELSE 0
        END AS upper_a,
        CASE
            WHEN b.type = 'Warning' THEN count(b.type) ELSE 0
        END AS warning
        FROM aircraft_aircraft b
        GROUP BY b.aircraft,b.type) query1
        GROUP BY query1.aircraft
        UNION
        SELECT 
        SUM(query1.info_count) info_count,
        SUM(query1.error_count) error_count,
        query1.status as name,
        SUM(query1.legend) legend,
        SUM(query1.lower_a) lower_a,
        SUM(query1.lower_b) lower_b,
        SUM(query1.paired_a) paired_a,
        SUM(query1.paired_b) paired_b,
        SUM(query1.pre_legend) pre_legend,
        SUM(query1.repeat_legend) repeat_legend,
        SUM(query1.upper_a) upper_a,
        SUM(query1.warning) warning,
        null as aircraft,
        null as type,
        query1.status as status,
        null as id
        FROM 
        (SELECT  DISTINCT(b.status), COUNT(b.type) AS count_type,b.type,
        SUM(b.info_count) as info_count, 
        SUM(b.errors_count) as error_count,
        CASE
            WHEN b.type = 'Legend' THEN count(b.type) ELSE 0
        END AS legend,
        CASE
            WHEN b.type = 'Lower A' THEN count(b.type) ELSE 0
        END AS lower_a,
        CASE
            WHEN b.type = 'Lower B' THEN count(b.type) ELSE 0
        END AS lower_b,
        CASE
            WHEN b.type = 'Paired A' THEN count(b.type) ELSE 0
        END AS paired_a,
        CASE
            WHEN b.type = 'Paired B' THEN count(b.type) ELSE 0
        END AS paired_b,
        CASE
            WHEN b.type = 'PreLegend' THEN count(b.type) ELSE 0
        END AS pre_legend,
        CASE
            WHEN b.type = 'Repeat Legend' THEN count(b.type) ELSE 0
        END AS repeat_legend,
        CASE
            WHEN b.type = 'Upper A' THEN count(b.type) ELSE 0
        END AS upper_a,
        CASE
            WHEN b.type = 'Warning' THEN count(b.type) ELSE 0
        END AS warning
        FROM aircraft_aircraft b
        GROUP BY b.status,b.type) query1
        GROUP BY query1.status
        UNION
        SELECT 
        SUM(query1.info_count) info_count,
        SUM(query1.error_count) error_count,
        query1.type as name,
        SUM(query1.legend) legend,
        SUM(query1.lower_a) lower_a,
        SUM(query1.lower_b) lower_b,
        SUM(query1.paired_a) paired_a,
        SUM(query1.paired_b) paired_b,
        SUM(query1.pre_legend) pre_legend,
        SUM(query1.repeat_legend) repeat_legend,
        SUM(query1.upper_a) upper_a,
        SUM(query1.warning) warning,
        null as aircraft,
        query1.type as type,
        null as status,
        null as id
        FROM 
        (SELECT  DISTINCT(b.status), COUNT(b.type) AS count_type,b.type,
        SUM(b.info_count) as info_count, 
        SUM(b.errors_count) as error_count,
        CASE
            WHEN b.type = 'Legend' THEN count(b.type) ELSE 0
        END AS legend,
        CASE
            WHEN b.type = 'Lower A' THEN count(b.type) ELSE 0
        END AS lower_a,
        CASE
            WHEN b.type = 'Lower B' THEN count(b.type) ELSE 0
        END AS lower_b,
        CASE
            WHEN b.type = 'Paired A' THEN count(b.type) ELSE 0
        END AS paired_a,
        CASE
            WHEN b.type = 'Paired B' THEN count(b.type) ELSE 0
        END AS paired_b,
        CASE
            WHEN b.type = 'PreLegend' THEN count(b.type) ELSE 0
        END AS pre_legend,
        CASE
            WHEN b.type = 'Repeat Legend' THEN count(b.type) ELSE 0
        END AS repeat_legend,
        CASE
            WHEN b.type = 'Upper A' THEN count(b.type) ELSE 0
        END AS upper_a,
        CASE
            WHEN b.type = 'Warning' THEN count(b.type) ELSE 0
        END AS warning
        FROM aircraft_aircraft b
        GROUP BY b.status,b.type) query1
        GROUP BY query1.type;
        """
   
    def get(self, request, *args, **kwargs):
        to_json=[]
        data=Aircraft.objects.raw(self.q)
        for e in data:
            to_json.append({
                'aircraft': e.aircraft,
                'status': e.status,
                'type': e.type,
                'info_count': e.info_count,
                'errors_count':e.error_count,
                'pre_legend': e.pre_legend,
                'warning': e.warning,
                'paired_b': e.paired_b,
                'legend': e.legend,
                'lower_b': e.lower_b,
                'repeat_legend': e.repeat_legend,
                'upper_a': e.upper_a,
                'lower_a': e.lower_a,
                'paired_a': e.paired_a
            
            })
            
        return Response(to_json,status=status.HTTP_200_OK)

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

    