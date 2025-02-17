from django.urls import path

from .views import PostTemplateView, post, posts

urlpatterns = [
    path('', posts),
    path('class-view/', PostTemplateView.as_view()),
    path('<str:slug>/', post),
]
