
from django.contrib import admin
from django.urls import path,include
from .views import getMessage
urlpatterns = [
    
    path('getMessage/', getMessage.as_view()),

]
