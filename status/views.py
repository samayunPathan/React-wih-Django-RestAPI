from status.models import Status # model
from .serializers import StatusSerializer # serialize based status model

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class StatusAPIView(APIView):

    def get(self,request,format=None):
        status_list=Status.objects.all()
        status_serializer=StatusSerializer(status_list,many=True)
        return Response(status_serializer.data)
