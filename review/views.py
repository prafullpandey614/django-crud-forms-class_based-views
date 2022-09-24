from dataclasses import dataclass
# from msilib.schema import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from matplotlib.style import context
from .forms import ReviewForm
from .models import Review
from django.views import View 
from django.views.generic import TemplateView , ListView
# # Create your views here.
# def review(models.Model):
#     pass
class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request,'reviews/index.html',{"form":form})
    def post(self,request):
        form = ReviewForm(request.POST)
        #if we want to update the review then we need to pass another parameter here
            # existing data = Review.objects.get(id=request.POST.get('id'))
            # form = ReviewForm(request.POST, instance=existing_data)
            #form.save() 
        
        if(form.is_valid()):
            # data_dictionary = form.cleaned_data
            # data = Review(user_name = data_dictionary['user_name'], email = data_dictionary['email'])
            # data.save()
            
            # The above lines are commented out because they need to be used when use forms.Form class in forms.py but instead we are using forms.ModelForm so we cna directly use save method here
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request,'reviews/index.html',{"form":form})
        
# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         #if we want to update the review then we need to pass another parameter here
#             # existing data = Review.objects.get(id=request.POST.get('id'))
#             # form = ReviewForm(request.POST, instance=existing_data)
#             #form.save() 
        
#         if(form.is_valid()):
#             # data_dictionary = form.cleaned_data
#             # data = Review(user_name = data_dictionary['user_name'], email = data_dictionary['email'])
#             # data.save()
            
#             # The above lines are commented out because they need to be used when use forms.Form class in forms.py but instead we are using forms.ModelForm so we cna directly use save method here
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#     else:
#         form = ReviewForm()
#     return render(request,'reviews/index.html',{"form":form})

class ThankYouView(TemplateView):
    template_name = "reviews/formd.html"
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs) #super method keeps all the previous data saved from parent class TemplateView
        context["message"] = "This Context in templateView is Working Properly"
        return context
class AllReviewsView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "data"
    # def get_context_data(self, **kwargs) :
    #     context =  super().get_context_data(**kwargs)
    #     data = Review.objects.all()
    #     context["data"] = data
    #     return context
class SingleReviewView(TemplateView):
    template_name = "reviews/single_data.html"
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        id = kwargs["id"]
        selected_person = Review.objects.get(pk=id)
        context["data"] = selected_person
        return context
# def thank_you(request):
#     return render(request,'reviews/formd.html')