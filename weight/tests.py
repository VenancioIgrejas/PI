from django.test import TestCase
from .models import WeightModel
from .serializers import WeightSerializer
# Create your tests here.


class ViewrModelsTest():
    querySet = WeightModel.objects.all()

    serializer = WeightSerializer(querySet)

    print(serializer.data)

