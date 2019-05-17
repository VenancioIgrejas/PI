from rest_framework import serializers
from .models import WeightModel

class WeightSerializer(serializers.Serializer):
    weight = serializers.FloatField()
    owner  = serializers.CharField(max_length=200,read_only=True)
    date = serializers.DateTimeField()

    def create(self, validate_data):
        return WeightModel.objects.create(**validate_data)

    def to_representation(self, obj):
        return {
            'weight':[q.weight for q in obj],
            'date':[q.date.strftime('%Y-%m-%dT%H:%M:%SZ') for q in obj],
        }