
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import FoodItem, Rating
from django.contrib.auth.decorators import login_required
from .forms import FoodRatingForm
import csv
import pickle
import pandas as pd
import numpy as np

popular_df = pd.read_pickle(r"food_app\popular.pkl")
pt=pd.read_pickle(r"food_app\pt.pkl")
similarity_score=pd.read_pickle(r"food_app\similarity_score.pkl")
food=pd.read_pickle((r"food_app\food.pkl"))
rating_df = pd.read_csv(r"food_app\rating.csv")


@login_required
def index(request):
    try:
        allfood = FoodItem.objects.all()
        
        if request.method == 'POST':
            form = FoodRatingForm(request.POST)
            if form.is_valid():
                food_id = request.POST['food_id']
                rating = form.cleaned_data['rating']
                user_id = request.user.id
                food_item = FoodItem.objects.get(FoodID=food_id)
                rating_obj, created = Rating.objects.get_or_create(UserId=user_id, FoodID=food_item)
                rating_obj.Ratings = rating
                rating_obj.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                print(form.errors)
                return render(request, 'food_app/index.html', {'allfood': allfood, 'form': form})
        else:
            form = FoodRatingForm()
            return render(request, 'food_app/index.html', {'allfood': allfood, 'form': form})
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print('*****')
        print(e)
        return render(request, 'food_app/error.html', {'error_message': error_message})

@login_required
def view_food(request,FoodID):
    try:
        view_food=FoodItem.objects.get(FoodID=FoodID)
        
        if request.method == 'POST':
            form = FoodRatingForm(request.POST)
            if form.is_valid():
                food_id = request.POST['food_id']
                rating = form.cleaned_data['rating']
                user_id = request.user.id
                food_item = FoodItem.objects.get(FoodID=food_id)
                rating_obj, created = Rating.objects.get_or_create(UserId=user_id, FoodID=food_item)
                rating_obj.Ratings = rating
                rating_obj.save()
                
                return HttpResponseRedirect(reverse('view_food'))
            else:
                print(form.errors)
                return render(request, 'food_app/view_food.html', {'view_food': view_food, 'form': form})
        else:
            form = FoodRatingForm()
            return render(request, 'food_app/view_food.html', {'view_food': view_food, 'form': form})
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print ('*****')
        print(e)
        return render(request, 'food_app/error.html', {'error_message': error_message})

@login_required
def about(request):
         allfood=FoodItem.objects.all()
    
         return render(request, 'food_app/about.html',{'allfood':allfood})

@login_required
def popular_food(request):
   
    try:

        if 'FoodName' in popular_df.columns:
            # Extract the 'FoodName' column as a list
            food_id = popular_df['FoodID'].to_list()
            food_name = popular_df['FoodName'].to_list()
            num_of_ratings = popular_df['num_ratings'].to_list()
            ratings = popular_df['avg_ratings'].to_list()
            category = popular_df['Category'].to_list()
            calories = popular_df['Total Calories(Cal)'].to_list()
            image = popular_df['Image'].to_list()
            ingredients = popular_df['Ingredients'].to_list()

            food_data = list(zip(food_id,food_name, num_of_ratings, ratings, category, calories, image, ingredients))

            if request.method == 'POST':
                form = FoodRatingForm(request.POST)
                if form.is_valid():
                    
                    food_id = request.POST['food_id']
                    
                    rating = form.cleaned_data['rating']
                    user_id = request.user.id
                    
                    food_item = FoodItem.objects.get(FoodID=food_id)
                   
                    rating_obj, created = Rating.objects.get_or_create(UserId=user_id, FoodID=food_item)
                    rating_obj.Ratings = rating
                    rating_obj.save()
                    
                    return HttpResponseRedirect(reverse('index'))
                else:
                    print(form.errors)
                    return render(request, 'food_app/popular_food.html', {'food_data': food_data, 'form': form})

            else:
                form = FoodRatingForm()
                return render(request, 'food_app/popular_food.html', {'food_data': food_data, 'form': form})

        else:
            error_message = "The 'FoodName' column is missing in the DataFrame."
            
            return render(request, 'food_app/error.html', {'error_message': error_message})

    except FileNotFoundError:
        error_message = "The 'popular.pkl' file is not found."
        
        return render(request, 'food_app/error.html', {'error_message': error_message})

    except Exception as e:

        error_message = f"An error occurred: {str(e)}"
        print('*****')
        print(e)
        return render(request, 'food_app/error.html', {'error_message': error_message})



@login_required
def recommend(request):
    return render(request, 'food_app/recommend.html')

@login_required
def recommend_food(request):
    allfood = FoodItem.objects.all()
    
    food_user_input = request.POST.get('food_user_input')
    matching_items = [item for item in pt.index if food_user_input.lower() in item.lower()]

    if matching_items:
        data = []
        for matched_item in matching_items:
            index = np.where(pt.index == matched_item)[0][0]
            similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=False)[1:6]
            for i in similar_items:
                item = []
                temp_df = food[food['FoodName'] == pt.index[i[0]]]
                item.extend(list(temp_df.drop_duplicates('FoodName')['FoodName'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['Category'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['Total Calories(Cal)'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['Carbs(g)'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['Fat(g)'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['Protein(g)'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['ServingSize'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['Image'].values))
                item.extend(list(temp_df.drop_duplicates('FoodName')['Ingredients'].values))
                data.append(item)
        
        return render(request, 'food_app/recommend.html', {'data': data, 'allfood': allfood})
    else:
        return render(request, 'food_app/error.html')