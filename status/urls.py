from django.urls import path
from status.views import StatusAPIView
from status.views import StatusListAPIView,StatusCreateAPIView,StatusDetailAPIView,StatusUpdateAPIView,StatusDeleteAPIView

urlpatterns=[
    path('status/',StatusAPIView.as_view()),
    path('status/list/',StatusListAPIView.as_view()), 
    path('status/create/',StatusCreateAPIView.as_view()),
    path('status/detail/<id>',StatusDetailAPIView.as_view()),
    path('status/update/<id>',StatusUpdateAPIView.as_view()),
    path('status/delete/<id>',StatusDeleteAPIView.as_view()),
]