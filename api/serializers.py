from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Post


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email address already exists.")
    return value


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(validators=[validate_email])

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.password = make_password(password)
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
            'email': {'required': True},
            'username': {'required': True},
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'post_date']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
        }

    def create(self, validated_data):

        user_id = self.context['request'].data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid user_id')

        post = Post.objects.create(user=user, **validated_data)
        return post
