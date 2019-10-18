from django.db import models

class TreiningTopic(models.Model):
    trening_topic = models.CharField(max_length=50)

    def __str__(self):
        return self.trening_topic

class TreningChoice(models.Model):
    treningChoiceQuestion = models.ForeignKey(TreiningTopic, on_delete=models.CASCADE)
    treningChoiceDescribe = models.CharField(max_length = 200)

    def __str__(self):
        return self.treningChoiceDescribe