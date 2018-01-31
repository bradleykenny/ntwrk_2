from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# ===== PROFILE ===== #

class Profile(models.Model):
    COLORS = (
        ('BLUE', "Blue"),
        ('GREEN', "Green"),
        ('RED', "Red"),
        ('PURPLE', "Purple"),
        ('YELLOW', "Yellow"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=6, choices=COLORS, default='BLUE')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# ===== FOLLOWING ===== #

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.follower, self.following)

User.add_to_class('following', models.ManyToManyField('self', through=Follow, related_name='followers', symmetrical=False))
