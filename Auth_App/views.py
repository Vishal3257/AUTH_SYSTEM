from drf_spectacular.utils import extend_schema
from datetime import timedelta
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from Auth_App.serializers import OTPRequestSerializer, OTPVerifySerializer, UserSerializer

# Create your views here.
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
@extend_schema(tags=['User Management'])
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@extend_schema(tags=['Security & Verification'])
@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp(request):
    serializer = OTPRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
            user.generate_otp()  # Already saves the OTP, no need for separate save()
            subject = 'OTP'
            expire_time = user.otp_created_at + timedelta(minutes=5)
            message = f'Your OTP is: {user.otp}'
            from_email = settings.DEFAULT_FROM_EMAIL
            try:
                send_mail(subject, message, from_email, [email], fail_silently=False)
            except Exception as e:
                return Response({'error': f'Failed to send OTP: {str(e)}'}, status=500)
            return Response({'message': 'OTP sent successfully', 'expire_time': expire_time}, status=200)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=404)
    return Response(serializer.errors, status=400)


@extend_schema(tags=['Authentication'])
@api_view(['POST'])
@permission_classes([AllowAny])
def login_verify_otp(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email)
            # Check if OTP exists
            if not user.otp:
                return Response({'error': 'No OTP generated. Please request OTP first.'}, status=400)
            # Check if OTP is still valid (within 5 minutes)
            if not user.is_otp_valid():
                user.otp = None
                user.save()
                return Response({'error': 'OTP expired. Please request a new OTP.'}, status=400)
            # Check if OTP matches
            if str(user.otp) == str(otp):
                user.otp = None   
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                return Response({'message': 'OTP verified successfully', 'token': token.key}, status=200)
            else:
                return Response({'error': 'Invalid OTP'}, status=400)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=404)
    return Response(serializer.errors, status=400)


@extend_schema(tags=['Authentication'])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.otp = None
    request.user.save()
    try:
        request.user.auth_token.delete()
    except Exception:
        pass
    return Response({'message': 'Logged out successfully'}, status=200)

