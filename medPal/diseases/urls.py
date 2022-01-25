from django.urls import path

from medPal.diseases import views
from medPal.diseases.views import CategoriesView, DiseaseView, CategoryView

urlpatterns = (
    path('', CategoriesView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryView.as_view(), name='category'),
    path('disease/<int:pk>', DiseaseView.as_view(), name='disease'),
)
