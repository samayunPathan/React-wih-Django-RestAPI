from status.models import Status # model
from .serializers import StatusSerializer # serialize based status model

# Create your views here.

# from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics,mixins

class StatusListCreateView(generics.ListCreateAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer


class StatusRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'



# class StatusListCreateView(mixins.CreateModelMixin,generics.ListAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer

#     def post(self,request,*args,**kwargs):
#         return self.create(request, *args, **kwargs)

# class StatusDetailUpdateDaleteView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request, *args, **kwargs)









# class StatusDetailAPIView(generics.RetrieveAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'

# class StatusUpdateAPIView(generics.UpdateAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'

# class StatusDeleteAPIView(generics.DestroyAPIView):
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'
