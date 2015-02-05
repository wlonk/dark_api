from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)

from django.contrib.auth.models import User


def get_user_for_object(obj):
    if obj.__class__ == User:
        return obj
    elif hasattr(obj, 'parent'):
        return get_user_for_object(obj.parent)
    else:
        return None


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = get_user_for_object(obj)
        return (
            request.method in SAFE_METHODS
            or request.user
            and request.user == user
        )
