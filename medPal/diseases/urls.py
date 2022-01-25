from django.urls import path

from medPal.diseases import views

urlpatterns = (
    path('', views.categories, name='categories'),
    path('category/<int:pk>', views.category, name='category'),
    path('disease/<int:pk>', views.disease, name='disease'),
    path('search/', views.search_disease, name='search disease'),
)
