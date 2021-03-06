from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.contrib.auth.models import User

from .serializers import UserSerializer, CourseSerializer, TrackableItemSerializer

from .models import Course, TrackableItem


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
    permission_classes = [AllowAny]

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


class CourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        courses = Course.objects.all()
        serializers = CourseSerializer(courses, many=True)
        return Response(serializers.data)

    def post(self, request):
        course = request.data
        # get the authenticated user from the token
        course['instructor'] = request.user.id
        print(course)
        serializers = CourseSerializer(data=course)
        if serializers.is_valid(raise_exception=ValueError):
            serializers.save()
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


class TrackableItemAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        # filter top level trackable items
        trackable_items = TrackableItem.objects.filter(trackable_items__isnull=True)
        serializers = TrackableItemSerializer(trackable_items, many=True)
        return Response(serializers.data)


class TrackableItemSubAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # get the parent Trackable Item
        id = self.request.query_params.get("id", None)
        print("id : ", id)
        if id:
            trackable_items = TrackableItem.objects.filter(trackable_items__id=id)
            serializers = TrackableItemSerializer(trackable_items, many=True)
            return Response(serializers.data)
        else:
            return Response([])