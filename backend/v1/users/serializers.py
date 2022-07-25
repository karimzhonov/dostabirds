from rest_framework.serializers import ModelSerializer
from .models import User


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)

