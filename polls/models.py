import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # the CharField requires that the max_length argument
    # be provided with a value.
    question_text = models.CharField(max_length=200)
    # every field type takes an option first paremeter
    # which represents a "verbose field name." This is
    # how the field will appear in things like the
    # admin interface.
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    # admin_ordered_field defines what the method uses to calculate it's value.
    # Specifying that the method is derived from 'pub_date' will allow users
    # to click on the Admin column heading "Published Recently?" and see the
    # results ordered appropriately.
    was_published_recently.admin_ordered_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published Recently?"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
