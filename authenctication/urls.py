from django.urls import path
from .views import GenesisAPIView

app_name="authentication"
# yu = true
urlpatterns =[
    path("gen", GenesisAPIView.as_view(), name="genesis"),
]