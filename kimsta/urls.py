from django.urls import path
from .import views


#urls
urlpatterns = [
    path('', views.insta, name='insta'),
]