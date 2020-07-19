from django.urls import path
from posts.views import HomePageView, DetailPageView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home' ),
    path('post/<int:pk>/', DetailPageView.as_view(), name ='post_detail'),
    path('post/new', BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post_delete'),
]