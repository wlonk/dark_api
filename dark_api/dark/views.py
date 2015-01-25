from django.contrib.auth import get_user_model
from rest_framework import (
    status,
    views,
    viewsets,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    UserWithTokenSerializer,
)

User = get_user_model()


class AuthenticateView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserWithTokenSerializer(data=request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username',)
