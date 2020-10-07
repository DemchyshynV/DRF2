from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EmployeeModel, OfficeModel
from .serializers import OfficeSerializer, EmployeeSerializer


class OfficeView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, *args, **kwargs):
        vasia = OfficeModel.objects.get(pk=3)
        serializer = OfficeSerializer(instance=vasia, data={'name': 'Asus', 'city': 'Rivne'})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        manager = EmployeeModel.objects
        qs = manager.filter(office__name='Apple')
        data = EmployeeSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
