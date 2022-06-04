from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Skill(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="Skill Name")
    strength = models.FloatField(verbose_name="Skill Strength",
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name} - {self.strength}"

    class Meta:
        verbose_name_plural = "Skills"


class Project(models.Model):
    name = models.CharField(max_length=256, verbose_name="Project Name", unique=True)
    description = models.TextField()
    year = models.IntegerField(verbose_name="Project Year")
    is_personal = models.BooleanField(default=False)