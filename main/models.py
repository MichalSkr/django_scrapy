from django.db import models


class Content(models.Model):
    """
    The scrapped data will be saved in this model
    """
    word = models.CharField(max_length=355)
    number = models.IntegerField()

    # class Meta:
    #     ordering = ('number',)