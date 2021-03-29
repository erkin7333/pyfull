from django.urls import path
from .views import MainIndex

url_name = "main"

urlpatterns = [
    path('', MainIndex.as_view(), name="index")
]
