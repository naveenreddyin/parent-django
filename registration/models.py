from django.db import models

# Create your models here.
class GoogleRegistrationId(models.Model):
    registration_id = models.CharField(max_length=255, null=False)


class UserProfile(models.Model):
    regid = models.OneToOneField(GoogleRegistrationId)
    type = models.IntegerField(null=False)


class User(models.Model):
    phone_no = models.CharField(max_length=254, unique=True)
    user_profile = models.OneToOneField(UserProfile)


class ConnectModel(models.Model):
    parent_device = models.ForeignKey(User, related_name="parent")
    child_device = models.OneToOneField(User, related_name="child")