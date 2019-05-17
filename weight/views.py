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
        
        # labels = ["Blue", "Yellow", "Green", "Purple", "Orange"]
        # default_items = [23, 2, 3, 12, 2]
        # data = {
        #         "labels": labels,
        #         "default": default_items,
        # }

        # return Response(data)


        querySet = WeightModel.objects.all()

        serializer = WeightSerializer(querySet)

        return Response(serializer.data)
