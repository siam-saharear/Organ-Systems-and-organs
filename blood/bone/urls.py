from django.urls import path
from . import views

urlpatterns = [
    # path("brain/", "views.brain", name= "brain")
    path("brain/", views.brain, name= "brain")
]
