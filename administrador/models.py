from django.db import models

# Create your models here.
class Project(models.Model):
    bathrooms_choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4'),
    )
    rooms_choice = (
        ('1', 'Individual'),
        ('2', 'Parejas'),
        ('3', '2 Adultos un niño'),
        ('4','4 Personas '),
        ('5','5 Personas '),
        ('6','Hasta 8 personas '),
    )
    title=models.CharField(max_length=100)
    cost=models.IntegerField()
    ubication=models.CharField(max_length=100)
    wifi=models.BooleanField()
    garage=models.BooleanField()
    pool=models.BooleanField()
    bathrooms=models.CharField(max_length=1, choices=bathrooms_choice)
    rooms=models.CharField(max_length=1, choices=rooms_choice)
    description=models.TextField()
    image=models.ImageField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)