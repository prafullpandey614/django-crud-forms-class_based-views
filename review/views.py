from dataclasses import dataclass
from re import T


# from msilib.schema import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from matplotlib.style import context
from .forms import ReviewForm
from .models import Review
from django.views import View 
from django.views.generic import TemplateView , ListView , DetailView ,FormView , CreateView
# # Create your views here.
# def review(models.Model):
#     pass
class ReviewView(CreateView):
    model = Review
    #create view automatically saves data to database that's why we use it but we also provide it form-class for customizations
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "/thank-you"
    #this is all we need to write for rendering  a Form in a template
    # def form_valid(self, form):
    #     form.save() #this function is used to save the form to the database
    #     return super().form_valid(form)
    # def get(self,request):
    #     form = ReviewForm()
    #     return render(request,'reviews/index.html',{"form":form})
    # def post(self,request):
    #     form = ReviewForm(request.POST)
    #     #if we want to update the review then we need to pass another parameter here
    #         # existing data = Review.objects.get(id=request.POST.get('id'))
    #         # form = ReviewForm(request.POST, instance=existing_data)
    #         #form.save() 
        
    #     if(form.is_valid()):
    #         # data_dictionary = form.cleaned_data
    #         # data = Review(user_name = data_dictionary['user_name'], email = data_dictionary['email'])
    #         # data.save()
            
    #         # The above lines are commented out because they need to be used when use forms.Form class in forms.py but instead we are using forms.ModelForm so we cna directly use save method here
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')
    #     return render(request,'reviews/index.html',{"form":form})
        
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
class SingleReviewView(DetailView):
    template_name = "reviews/single_data.html"
    model = Review
    context_object_name = "data" #by default here you can use "object" or "review" {lowercase model name} but  I changed it to "data" 
    # def get_context_data(self, **kwargs) :
    #     context =  super().get_context_data(**kwargs)
    #     id = kwargs["id"]
    #     selected_person = Review.objects.get(pk=id)
    #     context["data"] = selected_person
    #     return context
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id = request.session.get('favourite_review')
       
        context["is_favourite"] = favourite_id==str(loaded_review.id)
        return context 
# def thank_you(request):
#     return render(request,'reviews/formd.html')
class FavouriteReview(View):
    def post(self,request):
        fav_rev = request.POST["is_favourite"]
        request.session["favourite_review"] = fav_rev
        return HttpResponseRedirect("/review/" + fav_rev)
        