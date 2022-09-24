from django.urls import path
from . import views
urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you",views.ThankYouView.as_view()),
    path("all-data",views.AllReviewsView.as_view(), name="all-data"),
    path("review/<int:id>",views.SingleReviewView.as_view()),
]
