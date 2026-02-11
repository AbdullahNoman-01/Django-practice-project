from django.db import models

# Create your models here.
class student(models.Model):
   id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=50)
   address = models.TextField()
   fathar_name = models.TextField(default="Rahim Uddin")

   def __str__(self):
      return f"roll: {self.id} - {self.name}"
