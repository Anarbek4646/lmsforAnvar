from django.shortcuts import render
from django.http import HttpResponse
import requests as req


def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')


def cat_fact(request):
    response = req.get('https://catfact.ninja/fact')
    fact = response.json()['fact']
    return HttpResponse(fact)

