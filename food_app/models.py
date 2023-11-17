
from django.db import models   

class FoodItem(models.Model):
    FoodID = models.PositiveIntegerField(primary_key=True)
    FoodName = models.CharField(max_length=255)
    ServingSize = models.CharField(max_length=50)
    Carbs = models.DecimalField(max_digits=10, decimal_places=2)
    Fat = models.DecimalField(max_digits=10, decimal_places=2)
    Protein = models.DecimalField(max_digits=10, decimal_places=2)
    TotalCalories = models.PositiveIntegerField()
    Category = models.CharField(max_length=100)
    Ingredients = models.TextField() 
    Image = models.URLField()
    Type=models.CharField(max_length=30,default="Dinner")
    Veg_NonVeg=models.CharField(max_length=20,default="Veg")

    def __str__(self):
        return self.FoodName

class Rating(models.Model):
    UserId = models.PositiveIntegerField(default=1)
    FoodID = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    Ratings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"User {self.UserId} - Food {self.FoodID.FoodName} - Rating {self.Ratings}"
    


