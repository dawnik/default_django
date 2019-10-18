from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=20)
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    choice_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    def __str__(self):
        return self.choice_text



# Dodanie metod __str__() do twoich modeli jest ważne, nie tylko dla twojej własnej wygody, gdy używasz interaktywnego
# prompta, ale także dlatego, że reprezentacje obiektów są używane w automatycznie generowanym panelu administracyjnym Django.