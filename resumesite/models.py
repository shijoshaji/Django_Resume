from django.db import models

# Create your models here.


class SocialMedia(models.Model):
    title = models.CharField(max_length=50)
    mediaURL = models.CharField(max_length=500)
    iconClass = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
