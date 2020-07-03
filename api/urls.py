from django.urls import path
from .views import (UserRecordView,
                    CreateUserView,
                    CourseAPIView,
                    TrackableItemAPIView,
                    TrackableItemSubAPIView)


app_name = 'api'

urlpatterns = [
    path('user', UserRecordView.as_view(), name='users'),
    path('create-user', CreateUserView.as_view(), name='create-user'),
    path('course', CourseAPIView.as_view(), name='course'),
    path('trackable-item', TrackableItemAPIView.as_view(), name='trackable-item'),
    path('trackable-sub', TrackableItemSubAPIView.as_view(), name='trackable-sub'),

]
