from rest_framework import viewsets
from main.serializers import StatsSerializer


from main.models import Content


class StatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows content to be viewed.
    """
    queryset = Content.objects.all()
    serializer_class = StatsSerializer
