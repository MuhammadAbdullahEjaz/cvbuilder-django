from enum import unique
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, MaxValueValidator

# Create your models here.

class Profile(models.Model):

    phoneRegex = RegexValidator(regex=r"\+92\d{10}$")

    user = models.ForeignKey(get_user_model(), related_name="profile", on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    phone = models.CharField(max_length=13, validators=[phoneRegex,])

    def __str__(self) -> str:
        return f"{self.user} - {self.name}"


class Education(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="education", on_delete=models.CASCADE)
    DEGREE_TYPES = [('M', 'Matric'),
            ('I', 'Intermediated'),
            ('G', 'Graduation'),
            ('P', 'Master')]
    degree = models.CharField(max_length=1, choices=DEGREE_TYPES)
    school = models.CharField(max_length=32)
    percentage = models.PositiveIntegerField (validators=[MaxValueValidator(100),], default=0)
    ed_from = models.DateField()
    ed_to = models.DateField()

    def __str__(self) -> str:
        return f"{self.user} - {self.get_degree_display()}"

    class Meta:
        unique_together = ('user','degree')

class Experience(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="experience", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128) 
    ex_from = models.DateField()
    ex_to = models.DateField()

    def __str__(self) -> str:
        return f"{self.user} - {self.title}"

    class Meta:
        unique_together = ('user', 'title', 'ex_from')

class Skill(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="skill", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(100),], default=0)

    def __str__(self) -> str:
        return f"{self.user} - {self.title}"

    class Meta:
        unique_together = ('user','title')

class Interest_Hobby(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="iorh", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    iorh = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.title}"

    class Meta:
        unique_together = ('user','title')
