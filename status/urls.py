from django.urls import path

from status.views import (
    StatusListCreateView,
    StatusRetrieveUpdateAPIView,
    )

urlpatterns=[
    path('status/',StatusListCreateView.as_view()),
    path('status/detail/<id>',StatusRetrieveUpdateAPIView.as_view()),
   
]