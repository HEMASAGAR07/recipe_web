from django.db import models
class recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_discription = models.TextField()
    recpie_image=models.ImageField(upload_to="recipe")
# Create your models here.
