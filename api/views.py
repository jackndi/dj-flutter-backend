from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User


class UserRecordView(APIView):
    """
    Api view to get the list of all the registered users.
    GET request get the list of all the registered users whreas
    a POST request allow to create a new user
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)


class CreateUserView(APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid(raise_exception=ValueError):
            serializers.create(validate_data=request.data)
            return Response(
                serializers.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializers.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
