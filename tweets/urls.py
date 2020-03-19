
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('', )

urlpatterns = [
    path('tweets/', views.ListTweetsView.as_view()),
    path('retweets/all/', views.RetweetTweets.as_view()),
    path('create/tweets/', views.CreateTweets.as_view()),
    
]
