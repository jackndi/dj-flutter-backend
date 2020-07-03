from django.urls import path
from .views import (UserRecordView,
                    CreateUserView,
                    CourseAPIView,
                    TrackableItemAPIView)


app_name = 'api'

urlpatterns = [
    path('user', UserRecordView.as_view(), name='users'),
    path('create-user', CreateUserView.as_view(), name='create-user'),
    path('course', CourseAPIView.as_view(), name='course'),
    path('trackable-item', TrackableItemAPIView.as_view(), name='trackable-item'),

]
