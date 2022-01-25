
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medPal.home.urls')),
    path('', include('medPal.profiles.urls')),
    path('flashcards/', include('medPal.flashcards.urls')),
    path('diseases/', include('medPal.diseases.urls')),
]
