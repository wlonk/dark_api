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


class RedactedEmailField(serializers.EmailField):
    def to_representation(self, *args, **kwargs):
        request = self.context['request']
        ret = super(RedactedEmailField, self).to_representation(*args, **kwargs)
        if request.user.is_authenticated() and request.user.email == ret:
            return ret
        return ''


class UserSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='first_name')
    email = RedactedEmailField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'display_name',
            'email',
            'sheets',
        )
        read_only_fields = (
            'sheets',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
            'password',
        )
        extra_kwargs = {
            'pk': {
                'read_only': True,
            },
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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


class AceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AceCard


class FaceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceCard


class BaseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCard


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill


class SkillGroupSerializer(serializers.ModelSerializer):
    skills = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = SkillGroup
        fields = (
            'id',
            'name',
            'sheet',
            'skills',
        )


class SuitSerializer(serializers.ModelSerializer):
    ace = serializers.PrimaryKeyRelatedField(read_only=True)
    faceCards = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source="face_cards")
    baseCard = serializers.PrimaryKeyRelatedField(read_only=True, source="base_card")

    class Meta:
        model = Suit
        fields = (
            'id',
            'sheet',
            'name',
            'ace',
            'faceCards',
            'baseCard',
        )


class SheetSerializer(serializers.ModelSerializer):
    suits = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    skillGroups = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        source="skill_groups",
    )

    class Meta:
        model = Sheet
        fields = (
            'id',
            'user',
            'name',
            'look',
            'total_xp',
            'available_xp',
            'skillGroups',
            'suits',
        )
