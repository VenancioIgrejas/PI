# accounts/urls.py
from django.conf.urls import url, include
from django.views.generic.base import TemplateView

from .views import ChartDataView


urlpatterns = [
    #url(r'^api/data/$', get_data, name='api-data'),
    url(r'^dashbord', TemplateView.as_view(template_name='dashboard.html'), name='weight_dashbord'),
    url(r'^api/chart/data/$', ChartDataView.as_view(), name='api-data'),
]