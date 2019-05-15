# accounts/urls.py
from django.conf.urls import url, include

from .views import ChartDataView


urlpatterns = [
    #url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartDataView.as_view(), name='api-data'),
]