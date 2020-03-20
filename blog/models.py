
# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(_('título'), max_length=90)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

        

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

		
		

