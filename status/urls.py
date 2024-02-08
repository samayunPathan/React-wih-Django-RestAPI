from django.urls import path
from status.views import StatusAPIView

urlpatterns=[
    path('api/',StatusAPIView.as_view()),
]