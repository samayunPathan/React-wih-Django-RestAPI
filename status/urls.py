from django.urls import path
from status.views import StatusAPIView
from status.views import StatusListAPIView,StatusCreateAPIView

urlpatterns=[
    path('status/',StatusAPIView.as_view()),
    path('status/list/',StatusListAPIView.as_view()), 
    path('status/create/',StatusCreateAPIView.as_view())
]