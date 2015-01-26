from django.contrib.auth import get_user_model
from rest_framework import (
    status,
    views,
    viewsets,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import (
    Sheet,
    Suit,
    AceCard,
    FaceCard,
    BaseCard,
    SkillGroup,
    Skill,
)

from .serializers import (
    UserSerializer,
    UserWithTokenSerializer,
    SheetSerializer,
    SuitSerializer,
    AceCardSerializer,
    FaceCardSerializer,
    BaseCardSerializer,
    SkillGroupSerializer,
    SkillSerializer,
)

User = get_user_model()


class AuthenticateView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserWithTokenSerializer(data=request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username',)


class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class SuitViewSet(viewsets.ModelViewSet):
    queryset = Suit.objects.all()
    serializer_class = SuitSerializer


class AceCardViewSet(viewsets.ModelViewSet):
    queryset = AceCard.objects.all()
    serializer_class = AceCardSerializer


class FaceCardViewSet(viewsets.ModelViewSet):
    queryset = FaceCard.objects.all()
    serializer_class = FaceCardSerializer


class BaseCardViewSet(viewsets.ModelViewSet):
    queryset = BaseCard.objects.all()
    serializer_class = BaseCardSerializer


class SkillGroupViewSet(viewsets.ModelViewSet):
    queryset = SkillGroup.objects.all()
    serializer_class = SkillGroupSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
