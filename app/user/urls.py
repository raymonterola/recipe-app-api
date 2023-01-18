from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateUserTokenView.as_view(), name='token'),
    path('me/', views.UserProfileView.as_view(), name='me'),
]
