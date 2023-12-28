
from django.urls import path
from .views import a
urlpatterns = [
   path('الرئيسية/', a,name='home'),
]
