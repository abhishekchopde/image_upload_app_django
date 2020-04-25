from djongo import models
import jsonfield
from django.utils import timezone
# Create your models here.

class Images(models.Model):
    imageHash = models.CharField(max_length=32, default='default')  # md5 hash
    imageType = models.CharField(max_length=15, default='jpg')
    uploadedBy = jsonfield.JSONField()  # Should be changes to auth-token once auth is implemented
    uploadedAt = models.DateTimeField(default=timezone.now, null=True, blank=True)

    class Meta:
        db_table = 'images'
