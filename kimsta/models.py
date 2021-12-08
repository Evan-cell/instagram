import uuid
from django.db import models
from cloudinary.models import CloudinaryField

class posts(models.Model):
    # title field
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    caption = models.TextField(max_length=1500, verbose_name='Caption')
    #image field
    image = CloudinaryField('image')
    posted = models.DateTimeField(auto_now_add=True)
