from django.urls import path
from .views import UserRecordView, CreateUserView

app_name = 'api'

urlpatterns = [
    path('user', UserRecordView.as_view(), name='users'),
    path('create-user', CreateUserView.as_view(), name='create-user')
]
