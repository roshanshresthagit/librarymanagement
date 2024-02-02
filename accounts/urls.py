from django.urls import path
from .views import *

urlpatterns = [
    # path('', ListUsers.as_view(),name='listuser'),
    path('register/', CreateUser.as_view(),name='register'),
    path('viewusers/', ListUsers.as_view(),name='viewuser'),
    path('finduser/<int:pk>/', GetUserByIdView.as_view(),name='finduser'),

]
