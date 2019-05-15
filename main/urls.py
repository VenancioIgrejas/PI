from django.conf.urls import url
from . import views

app_name = 'main'  # here for namespacing of urls

urlpatterns = [
    url("", views.homepage, name="homepage"),
    url(r'^register/', views.register, name="register"),
    # url("logout", views.logout_request, name="logout"),
]
