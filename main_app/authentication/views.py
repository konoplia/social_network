from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from authentication.serializers import CustomUserSerializer


User = get_user_model()


class CustomUserView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_data_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(
            user_data_saved.username)}, status=status.HTTP_201_CREATED)
