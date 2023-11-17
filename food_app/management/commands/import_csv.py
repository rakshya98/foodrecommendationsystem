# # # yourappname/management/commands/import_csv.py
# # import csv
# # from django.core.management.base import BaseCommand
# # from food_app.models import FoodItem

# # class Command(BaseCommand):
# #     help = 'Import data from CSV file'

# #     def handle(self, *args, **kwargs):
# #         with open('food_app/foodreco.csv', 'r') as csvfile:
# #             reader = csv.reader(csvfile)
# #             next(reader)  # Skip the header row
# #             for row in reader:
# #                 obj = FoodItem(
# #                     FoodID = int(row[0]),
# #                     FoodName = row[1],
# #                     ServingSize = row[2],
# #                     Carbs = float(row[3]),
# #                     Fat = float(row[4]),
# #                     Protein = float(row[5]),
# #                     TotalCalories = int(row[6]),
# #                     Category = row[7],
# #                     Image = row[8],
# #                     Ingredients = row[9],
                    
# #                     # Set other fields accordingly
# #                 )
                
# #                 obj.save()


# # import csv
# # from django.core.management.base import BaseCommand
# # from food_app.models import FoodItem, Rating

# # class Command(BaseCommand):
# #     help = 'Import data from CSV files'

# #     def handle(self, *args, **kwargs):
# #         # Import FoodItem data from foodreco.csv
# #         with open('food_app/foodreco.csv', 'r') as csvfile:
# #             reader = csv.reader(csvfile)
# #             next(reader)  # Skip the header row
# #             for row in reader:
# #                 obj = FoodItem(
# #                     FoodID=int(row[0]),
# #                     FoodName=row[1],
# #                     ServingSize=row[2],
# #                     Carbs=float(row[3]),
# #                     Fat=float(row[4]),
# #                     Protein=float(row[5]),
# #                     TotalCalories=int(row[6]),
# #                     Category=row[7],
# #                     Image=row[8],
# #                     Ingredients=row[9],
# #                     # Set other fields accordingly
# #                 )
# #                 obj.save()

# #         # Import Rating data from ratings.csv
# #         with open('food_app/ratings.csv', 'r') as csvfile:
# #             reader = csv.reader(csvfile)
# #             next(reader)  # Skip the header row
# #             for row in reader:
# #                 obj = Rating(
# #                     UserId=int(row[0]),
# #                     FoodID=int(row[1]),
# #                     Ratings=int(row[2]),
# #                     # Set other fields accordingly
# #                 )
# #                 obj.save()



# # # myapp/management/commands/import_data.py
# # import csv
# # from django.core.management.base import BaseCommand
# # from food_app.models import FoodItem, Rating

# # class Command(BaseCommand):
# #     help = 'Import food data and ratings from CSV files'

# #     def add_arguments(self, parser):
# #         parser.add_argument('foodreco_csv', type=str, help='Path to the food CSV file')
# #         parser.add_argument('rating_csv', type=str, help='Path to the ratings CSV file')

# #     def handle(self, *args, **options):
# #         food_csv_path = options['foodreco_csv']
# #         ratings_csv_path = options['rating_csv']

# #         # Import food data from the food CSV file
# #         with open(food_csv_path, 'r', encoding='utf-8') as food_file:
# #             food_reader = csv.DictReader(food_file)
# #             for row in food_reader:
# #                 FoodItem.objects.create(
# #                     FoodID=row['FoodID'],
# #                     FoodName=row['FoodName'],
# #                     ServingSize=row['ServingSize'],
# #                     Carbs=row['Carbs(g)'],
# #                     Fat=row['Fat(g)'],
# #                     Protein=row['Protein(g)'],
# #                     TotalCalories=row['Total Calories(Cal)'],
# #                     Category=row['Category'],
# #                     Ingredients=row['Ingredients'],
# #                     Image=row['Image']
# #                 )

# #         # Import ratings data from the ratings CSV file
# #         with open(ratings_csv_path, 'r', encoding='utf-8') as ratings_file:
# #             ratings_reader = csv.DictReader(ratings_file)
# #             for row in ratings_reader:
# #                 Rating.objects.create(
# #                     UserId=row['UserId'],
# #                     FoodID_id=row['FoodID'],  # Assuming FoodID is an integer field
# #                     Ratings=row['Ratings']
# #                 )

# #         self.stdout.write(self.style.SUCCESS('Data imported successfully'))


# import csv
# from django.core.management.base import BaseCommand
# from food_app.models import FoodItem, Rating

# class Command(BaseCommand):
#     help = 'Import food data and ratings from CSV files'

#     def add_arguments(self, parser):
#         parser.add_argument('foodreco_csv', type=str, help='Path to the food CSV file')
#         parser.add_argument('blabfood_csv', type=str, help='Path to the ratings CSV file')

#     def handle(self, *args, **options):
#         food_csv_path = options['foodreco_csv']
#         ratings_csv_path = options['blabfood_csv']

#         # Create a dictionary to map FoodName to FoodID
#         food_name_to_id = {food.FoodName: food.FoodID for food in FoodItem.objects.all()}

#         # Import food data from the food CSV file
#         with open(food_csv_path, 'r', encoding='utf-8') as food_file:
#             food_reader = csv.DictReader(food_file)
#             for row in food_reader:
#                 food_name = row['FoodName']
#                 food_id = food_name_to_id.get(food_name)

#                 if food_id:
#                     # If the FoodName already exists, update the existing FoodItem
#                     FoodItem.objects.filter(FoodID=food_id).update(
#                         FoodName=row['FoodName'],
#                         ServingSize=row['ServingSize'],
#                         Carbs=row['Carbs(g)'],
#                         Fat=row['Fat(g)'],
#                         Protein=row['Protein(g)'],
#                         TotalCalories=row['Total Calories(Cal)'],
#                         Category=row['Category'],
#                         Ingredients=row['Ingredients'],
#                         Image=row['Image']
#                     )
#                 else:
#                     # If the FoodName does not exist, create a new FoodItem
#                     FoodItem.objects.create(
#                         FoodName=row['FoodName'],
#                         ServingSize=row['ServingSize'],
#                         Carbs=row['Carbs(g)'],
#                         Fat=row['Fat(g)'],
#                         Protein=row['Protein(g)'],
#                         TotalCalories=row['Total Calories(Cal)'],
#                         Category=row['Category'],
#                         Ingredients=row['Ingredients'],
#                         Image=row['Image']
#                     )

#         # Import ratings data from the ratings CSV file
#         with open(ratings_csv_path, 'r', encoding='utf-8') as ratings_file:
#             ratings_reader = csv.DictReader(ratings_file)
#             for row in ratings_reader:
#                 user_id = row['UserId']
#                 food_name = row['FoodID']
#                 rating = row['Ratings']

#                 # Get the corresponding FoodItem object using the FoodName
#                 food_id = food_name_to_id.get(food_name)

#                 if food_id:
#                     # Create the Rating record with the valid FoodItem reference
#                     Rating.objects.create(
#                         UserId=user_id,
#                         FoodID_id=food_id,
#                         Ratings=rating
#                     )
#                 else:
#                     self.stdout.write(self.style.WARNING(f'Skipped rating for unknown food: {food_name}'))

#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))


import csv
from django.core.management.base import BaseCommand
from food_app.models import FoodItem, Rating
from django.db.utils import IntegrityError  # Import IntegrityError for database errors

class Command(BaseCommand):
    help = 'Import food data and ratings from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('foodreco_csv', type=str, help='Path to the food CSV file')
        parser.add_argument('blabfood_csv', type=str, help='Path to the ratings CSV file')

    def handle(self, *args, **options):
        food_csv_path = options['foodreco_csv']
        ratings_csv_path = options['blabfood_csv']

        # Create a dictionary to map FoodName to FoodID
        food_name_to_id = {food.FoodName: food.FoodID for food in FoodItem.objects.all()}

        # Import food data from the food CSV file
        with open(food_csv_path, 'r', encoding='utf-8') as food_file:
            food_reader = csv.DictReader(food_file)
            for row in food_reader:
                food_name = row['FoodName']
                food_id = food_name_to_id.get(food_name)

                try:
                    if food_id:
                        # If the FoodName already exists, update the existing FoodItem
                        FoodItem.objects.filter(FoodID=food_id).update(
                            FoodName=row['FoodName'],
                            ServingSize=row['ServingSize'],
                            Carbs=row['Carbs(g)'],
                            Fat=row['Fat(g)'],
                            Protein=row['Protein(g)'],
                            TotalCalories=row['Total Calories(Cal)'],
                            Category=row['Category'],
                            Ingredients=row['Ingredients'],
                            Image=row['Image']
                        )
                    else:
                        # If the FoodName does not exist, create a new FoodItem
                        FoodItem.objects.create(
                            FoodName=row['FoodName'],
                            ServingSize=row['ServingSize'],
                            Carbs=row['Carbs(g)'],
                            Fat=row['Fat(g)'],
                            Protein=row['Protein(g)'],
                            TotalCalories=row['Total Calories(Cal)'],
                            Category=row['Category'],
                            Ingredients=row['Ingredients'],
                            Image=row['Image']
                        )
                except IntegrityError as e:
                    print("*****************************")
                    print(self.stdout.write(self.style.WARNING(f'Skipped duplicate entry: {food_name}')))

        # Import ratings data from the ratings CSV file
        with open(ratings_csv_path, 'r', encoding='utf-8') as ratings_file:
            ratings_reader = csv.DictReader(ratings_file)
            for row in ratings_reader:
                user_id = row['UserId']
                food_name = row['FoodID']
                rating = row['Ratings']

                # Get the corresponding FoodItem object using the FoodName
                food_id = food_name_to_id.get(food_name)

                try:
                    if food_id:
                        # Create the Rating record with the valid FoodItem reference
                        Rating.objects.create(
                            UserId=user_id,
                            FoodID_id=food_id,
                            Ratings=rating
                        )
                    else:
                        self.stdout.write(self.style.WARNING(f'Skipped rating for unknown food: {food_name}'))
                except IntegrityError as e:
                    print("*****************************")
                    print(self.stdout.write(self.style.WARNING(f'Skipped duplicate rating entry for food: {food_name}')))

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
