from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users', views.UserRetrieveUpdateAPIView.as_view()),
    path('api/v1/sign_up', views.RegistrationAPIView.as_view()),
    path('api/v1/sign_in', views.LoginAPIView.as_view()),
    path('api/v1/logout', views.LogoutView.as_view()),
]
