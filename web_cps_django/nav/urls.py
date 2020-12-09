from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from nav import views

urlpatterns = [
    path('nav/', views.List.as_view()),
    path('nav/<int:pk>/', views.Detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)