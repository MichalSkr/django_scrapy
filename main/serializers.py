from django.contrib.auth.models import User, Group
from rest_framework import serializers

from main.models import Content


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('word', 'number')