from django import forms
#newline
from food_app.models import FoodItem

class FoodRatingForm(forms.Form):
    # user_id=forms.CharField()
    # food_id=forms.CharField()
   #newline
    # food_item = forms.ModelChoiceField(queryset=FoodItem.objects.all())
    rating = forms.FloatField(label='Rating', min_value=1, max_value=10)
