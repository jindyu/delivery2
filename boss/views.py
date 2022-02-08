from turtle import done
from django.shortcuts import render
from order import serializers
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

# Create your views here.
@csrf_exempt
def order_list(request, shop):
    if request.method == 'GET':
        orders = Order.objects.filter(shop=shop)
        return render(request, 'boss/order_list.html', {'order_list':orders})
    else:
        return HttpResponse(status=404)

@csrf_exempt
def time_input(request):
    if request.method == 'POST':
        estimated_time = int(request.POST['estimated_time'])
        order_id = int(request.POST['order_id'])
        order_item = Order.objects.get(pk=order_id)
        order_item.estimated_time = estimated_time
        order_item.save()
        return render(request, 'boss/success.html', {'shop':order_item.shop.id})
    else:
        return HttpResponse(status=404)

