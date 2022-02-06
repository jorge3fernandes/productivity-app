from turtle import title
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class TwelveWeek(models.Model):
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class Goal(models.Model):
    tag_choices = (("physical", "Physical"), 
                   ("spiritual", "Spiritual"),
                   ("work", "Work"),
                   )
    
    TwelveWeek = models.ManyToManyField(TwelveWeek, blank = True)
    title = models.CharField(max_length=200)
    # description = models.TextField(max_length=1000)
    start_date = models.DateField(blank = True, null=True)
    end_date = models.DateField(blank = True, null=True)
    tags = models.CharField(choices= tag_choices, max_length=200, null=True, blank = True)

    def __str__(self):
        return self.title

class Tactic(models.Model):
    # status_choices = [['in progress', 'In Progress'],
    #                   ['not started', 'Not Started'],
    #                   ['completed', 'Completed']
    #                   ]
    frequency_choices = [['daily', 'Daily'],
                      ['weekly', 'Weekly'],
                      ['once', 'Once']
                      ]
    title = models.CharField(max_length=150)
    goal = models.ManyToManyField(Goal)
    description = models.TextField(max_length=1000, blank = True, null=True)
    start_date = models.DateField(blank = True, null=True)
    end_date = models.DateField(blank = True, null=True)
    frequency = models.CharField(max_length=50, choices=frequency_choices, default="once", blank = True, null=True)
    # status = models.CharField(max_length=150, choices=status_choices)
    score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], blank = True, null=True)

    def __str__(self):
        return self.title


class Week(models.Model):
    twelve_week = models.ForeignKey(TwelveWeek, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    tactic = models.ManyToManyField(Tactic)
    victories_successes = models.TextField(max_length=1000, verbose_name="What are you pleased with?", blank = True, null=True)
    breakdowns = models.TextField(max_length=1000, verbose_name="What are you concerned about?", blank = True, null=True)
    actions = models.TextField(max_length=1000, verbose_name="Insigths and Actions for next week.", blank = True, null=True)
    start_date = models.DateField(blank = True, null=True)
    end_date = models.DateField(blank = True, null=True)
    score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], blank = True, null=True)

    def __str__(self):
        return self.title

class Day(models.Model):
    twelve_week = models.ForeignKey(TwelveWeek, null=True, on_delete=models.SET_NULL)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    date = models.DateField()
    tactic = models.ManyToManyField(Tactic)
    reflection = models.TextField(max_length=1000, verbose_name="Reflection on the day!", blank = True, null=True)
    score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], blank = True, null=True)

    def __str__(self):
        return f"{self.twelve_week}_{self.week}_{self.date}"

