from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../user-icon_pdzqa4'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user_name}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_name=instance)


post_save.connect(create_profile, sender=User)
