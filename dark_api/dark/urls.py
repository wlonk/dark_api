from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    AceCardViewSet,
    AuthenticateView,
    BaseCardViewSet,
    FaceCardViewSet,
    RegistrationView,
    SheetViewSet,
    SkillGroupViewSet,
    SkillViewSet,
    SuitViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sheets', SheetViewSet)
router.register(r'suits', SuitViewSet)
router.register(r'ace-cards', AceCardViewSet)
router.register(r'face-cards', FaceCardViewSet)
router.register(r'base-cards', BaseCardViewSet)
router.register(r'skill-groups', SkillGroupViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
    url(
        r'^token-auth/$',
        AuthenticateView.as_view(),
        name='token-auth',
    ),
    url(
        r'^registration/$',
        RegistrationView.as_view(),
        name='registration',
    ),
    url(
        r'^api-auth',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^', include(router.urls)),
]
