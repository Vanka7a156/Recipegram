from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe-edit'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
]

