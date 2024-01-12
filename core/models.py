from __future__ import annotations

import uuid
from django.contrib.auth.models import User
from django.db import models


class Assurance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    prix_mensuel = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    contract = models.TextField()

    def __str__(self):
        return f"{self.type} - { self.prix_mensuel}"

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    _phone = models.IntegerField()
    _profession = models.CharField(max_length=255)
    _birthday = models.DateField()
    assurance_list = models.ForeignKey(Assurance, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.username}"

    @property
    def get_full_name(self) -> str:
        return f'{self.user.first_name} {self.user.username}'

    @property
    def phone(self) -> int:
        return int(self._phone)


class Activity(models.Model):
    nom = models.CharField(max_length=250)
    level = models.CharField(max_length=255)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.nom} {self.level}"


class Personnel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    _phone = models.IntegerField()
    _poste = models.CharField(max_length=255)
    _birthday = models.DateField()
    _salary = models.FloatField(default=0)
    activity_list = models.ManyToManyField(Activity)

    def __str__(self):
        return f"{self.user.first_name} {self.user.username}"

    @property
    def get_full_name(self) -> str:
        return f'{self.user.first_name} {self.user.username} '
