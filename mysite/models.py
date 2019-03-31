from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    edited_date=models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.FileField(null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING) #this is to display name of user who posted, for this we need to import
                                                                               #User at top and user at forms.py

  #but 'user' not working due to once deleted and migrated again from then error shoing during migrate

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mysite:detail', kwargs={'id':self.id})
