from django.urls import path
from . import views

urlpatterns = [
    path('getMe/', views.GetMe.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('get/<int:pk>/', views.UserGetView.as_view()),
    path('update/<int:pk>/', views.UserUpdateView.as_view())
]
