
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('tips', views.ContributePythonTipView)
router.register('likes', views.TweetLikeView)
router.register('bookmark', views.TweetBookmarkView)



urlpatterns = [
    path('', include(router.urls)),

    path('tweets/', views.ListTweetsView.as_view()),
    path('retweets/all/', views.RetweetTweets.as_view()),
    path('create/tweets/', views.CreateTweets.as_view()),
    path('tweet/<int:pk>/', views.TweetDetailView.as_view()),
    
]
