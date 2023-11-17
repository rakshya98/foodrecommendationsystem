# from food_app.models import FoodItem,Rating
# import csv
# from django.conf import settings
# from pathlib import Path
# from .models import Rating
# from django.shortcuts import HttpResponse
# file_path = Path.joinpath(settings.BASE_DIR,'food_app/rating.csv')
# def run(request):
#     with open(file_path) as file:
#         reader = csv.reader(file)
#         next(reader)  # Advance past the header
#         Rating.objects.all().delete()
#         for row in reader:
#             user_id,food_id,rating = row[0],row[1],row[2]
#             print( user_id,food_id,rating)
#             rating = Rating(UserId=user_id,FoodID_id=food_id,Ratings=int(float(rating)))
#             rating.save()
#     return HttpResponse("saved")



# from food_app.models import FoodItem, Rating
# import csv
# from django.conf import settings
# from pathlib import Path
# from django.shortcuts import HttpResponse

# file_path = Path.joinpath(settings.BASE_DIR, 'food_app/foodreco.csv')

# def run(request):
#     with open(file_path) as file:
#         reader = csv.reader(file)
#         next(reader)  # Advance past the header
#         FoodItem.objects.all()  # Clear existing data
#         for row in reader:
#             # Assign values to variables based on CSV column positions
#             FoodID, FoodName, ServingSize, Carbs, Fat, Protein, TotalCalories, Category, Ingredients,Image, Type, Veg_NonVeg = row

#             # Handle empty or non-numeric values
#             try:
#                 FoodID = int(FoodID) if FoodID else 0  
#                 Carbs = float(Carbs) if Carbs else 0.0
#                 Fat = float(Fat) if Fat else 0.0
#                 Protein = float(Protein) if Protein else 0.0
#                 TotalCalories = int(TotalCalories) if TotalCalories else 0
#             except (ValueError, TypeError):
#                 # Handle invalid or empty values here (e.g., set them to default values)
#                 FoodID=0
#                 Carbs = 0.0
#                 Fat = 0.0
#                 Protein = 0.0
#                 TotalCalories = 0

#             # Create and save a FoodItem object
#             food_item = FoodItem(
#                 FoodID=FoodID,
#                 FoodName=FoodName,
#                 ServingSize=ServingSize,
#                 Carbs=Carbs,
#                 Fat=Fat,
#                 Protein=Protein,
#                 TotalCalories=TotalCalories,
#                 Category=Category,
#                 Ingredients=Ingredients,
#                 Image=Image,
#                 Type=Type,
#                 Veg_NonVeg=Veg_NonVeg
#             )
#             food_item.save()
        
#     return HttpResponse("saved")