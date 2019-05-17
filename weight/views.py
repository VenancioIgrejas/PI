from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import WeightModel
from django.contrib.auth.models import User
from .serializers import WeightSerializer

# Create your views here.

class ChartDataView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []  # (authentication.TokenAuthentication,)
    permission_classes = []  # (permissions.IsAdminUser,)

    def get(self, request, format=None):
        # data = {
        #     'weight_values': [1, 4, 6, 6, 9, 7, 10, 12, 11],
        #     'weights_date': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        # }

        querySet = WeightModel.objects.all()

        serializer = WeightSerializer(querySet)

        return Response(serializer.data)
