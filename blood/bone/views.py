from django.shortcuts import render


def brain(response):
    return render(response, "bone/brain.html",{"context":"The brain has two hemisphere. Left and right hemesphere."})