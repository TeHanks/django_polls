from django.db import models

class Survey(models.Model):
    survey_name = models.CharField(max_length=100, verbose_name="Survey Name")

    def __str__(self):
        return self.survey_name

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, verbose_name="Question Text")
    question_type = models.CharField(max_length=2, choices=[("MC", "Multichoice"), ("TX", "Text")])

    def __str__(self):
        return self.question_text

class SurveyOptions(models.Model):

    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

# Create your models here.
