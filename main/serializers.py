from django.contrib.auth.models import User, Group
from rest_framework import serializers

from main.models import Content


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class StatsSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=355)
    number = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Content.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.word = validated_data.get('word', instance.word)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance