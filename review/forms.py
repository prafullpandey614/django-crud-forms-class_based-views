from pyexpat import model
from attr import field
from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=55, label="Apan Naam Ka Padi", error_messages={
#         "required": "Ae Mrde Naam Bhula gaila ka apan",
#         "max_length": "Aae ho dada hate chuka naam ba raur",
#     }, )
#     email = forms.EmailField(max_length=255)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ['']
        labels = {
            'user_name' : 'ka nam padi',
            'email' : 'email chalwe ni'
        }
        