from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField(max_length=500)
    posted_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
