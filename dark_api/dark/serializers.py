from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import (
    Sheet,
    Suit,
    AceCard,
    FaceCard,
    BaseCard,
    SkillGroup,
    Skill,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )


class UserWithTokenSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    token = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj['user'])
        return token.key

    def get_user_id(self, obj):
        return obj['user'].id

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError(
                        'User account is disabled.'
                    )
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError(
                    'Unable to login with provided credentials.'
                )
        else:
            raise serializers.ValidationError(
                'Must include "username" and "password"'
            )


class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet


class SuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suit


class AceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AceCard


class FaceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceCard


class BaseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCard


class SkillGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillGroup


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
