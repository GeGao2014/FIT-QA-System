from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def answer(self):
        return self.answer_text

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    answer.admin_order_field = 'ans'
    answer.boolean = True


class InputText(models.Model):
    question = models.ForeignKey(Question)
    input_text = models.CharField(max_length=200)

    def __str__(self):
        return self.input_text