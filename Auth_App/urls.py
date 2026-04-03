from django.urls import path
from Auth_App import views

urlpatterns = [
    path('api/register/', views.register, name='register'),
    path('api/send-otp/', views.send_otp, name='send_otp'),
    path('api/login-verify-otp/', views.login_verify_otp, name='login_verify_otp'),
    path('api/logout/', views.logout, name='logout'),
]