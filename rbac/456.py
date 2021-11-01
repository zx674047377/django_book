from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership', through_fields=('group', 'person'))

class Membership(models.Model):
    group = models.ForeignKey(Group)
    person = models.ForeignKey(Person)
    inviter = models.ForeignKey(Person, related_name="membership_invites")
    invite_reason = models.CharField(max_length=64)