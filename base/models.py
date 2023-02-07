import random
from django.db import models
from django.utils import timezone


def generate_pk():
    number = random.randint(100000, 999999)
    return "AA{}{}".format(timezone.now().strftime("%y%m%d"), number)


class Note(models.Model):
    id = models.CharField(
        default=generate_pk,
        primary_key=True,
        max_length=255,
        unique=True,
        editable=False,
    )
    title = models.CharField(null=True, max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
