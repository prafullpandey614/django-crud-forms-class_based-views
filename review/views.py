from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# # Create your views here.
# def review(models.Model):
#     pass
def review(request):
    if request.method == 'POST':
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
    else:
        form = ReviewForm()
    return render(request,'reviews/index.html',{"form":form})

def thank_you(request):
    return render(request,'reviews/formd.html')