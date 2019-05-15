from django.contrib import admin
from .models import WeightModel

myModels = [WeightModel]  # iterable list
admin.site.register(WeightModel)