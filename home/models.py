from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class Video(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    project_manager= models.CharField(max_length=100)
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    videoFile = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField( upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)