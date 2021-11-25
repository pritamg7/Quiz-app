from django.db import models
import random



class Quiz(models.Model):
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    

    def __str__(self):
        return f"{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())[:self.number_of_questions]
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'

