from django.shortcuts import render
from django.http import HttpResponse
import requests
from shop.models import Item, Purchase
from django.shortcuts import HttpResponse, redirect, render


def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')


def cat_fact(request):
    response = requests.get('https://catfact.ninja/fact')
    fact = response.json()['fact']
    return HttpResponse(fact)


def item_view(request):
    if request.method == "GET":
        items = Item.objects.all()

        context = {

            'items': items
        }

        return render(request, 'items.html', context=context)


def detail_view(request, id):
    if request.method == "GET":

        item = Item.objects.get(id=id)
        purchase = item.purchases.all()
        print(purchase)
        context = {
            'purchases': purchase
        }

        return render(request, 'detail.html', context=context)
