from requests import Response
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView

from smart_home.measurement.models import Measurement, Sensor
from smart_home.measurement.serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class SensorCreateView(ListCreateAPIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        sensor = Sensor(name=request.data['name'], description=request.data['description'])
        sensor.save()
        return Response('Датчик добавлен')


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = SensorDetailSerializer(Sensor.object.get(pk=pk), data=request.data)
        sensor.save()
        return Response('Данные обновлены')

    def get(self, request, pk):
        sensor = SensorDetailSerializer(Sensor.object.get(pk=pk))
        return Response(sensor.data)


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        new_measurement = MeasurementSerializer(data=request.data)
        new_measurement.save()
        return Response('Данные обновлены')