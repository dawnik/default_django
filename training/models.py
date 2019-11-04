from django.db import models
from django.utils import timezone
import datetime

class TrainingQuestion(models.Model):
    training_title = models.CharField(max_length=200)
    date_create_trainig = models.DateTimeField('date create training')

    def __str__(self):
        return self.training_title

    def was_published(self):
        return self.date_create_trainig >= timezone.now() - datetime.timedelta(days=1)