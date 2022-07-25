from django.urls import path, include
from .views import TestView

urlpatterns = [
    path('users/', include('v1.users.urls')),
    path('orders/', include('v1.orders.urls')),
    path('test/', TestView.as_view()),
]
