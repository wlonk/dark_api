from django.conf.urls import patterns, url, include
from rest_framework import routers

from .views import (
    UserViewSet,
    AuthenticateView,
    SheetViewSet,
    SuitViewSet,
    AceCardViewSet,
    FaceCardViewSet,
    BaseCardViewSet,
    SkillGroupViewSet,
    SkillViewSet,
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

urlpatterns = patterns('',  # NOQA
    url(
        r'^api-token-auth/$',
        AuthenticateView.as_view(),
        name='api-token-auth',
    ),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
)
