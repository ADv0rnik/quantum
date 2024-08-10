from django.urls import path
from .views import get_data


app_name = 'qa'

urlpatterns = [
    path("detector_filter/", get_data, name='datasheet')
]
