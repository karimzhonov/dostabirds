from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate, logout

from .models import User
from .serializers import UserDetailSerializer


class UserGetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserDetailSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not founded'}, status=status.HTTP_404_NOT_FOUND)


class UserCreateView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username, password=password)

        login(request, user)
        return Response(UserDetailSerializer(user).data, status=status.HTTP_201_CREATED)


class UserUpdateView(APIView):
    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserDetailSerializer(user)
        for key, value in request.data:
            if key in serializer.data.keys():
                setattr(user, key, value)
        user.save()
        return Response(UserDetailSerializer(user).data)


class GetMe(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response(UserDetailSerializer(request.user), status=status.HTTP_200_OK)
        return Response({})


class UserLoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            logout(request)
            login(request, user)
            return Response(UserDetailSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Username or password is incorrect'})
