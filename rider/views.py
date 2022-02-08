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
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        return render(request, 'rider/order_list.html', {'order_list':orders})
    elif request.method == 'POST':
        order_id = int(request.POST['order_id'])
        order_item = Order.objects.get(pk=order_id)
        order_item.deliver_finish = 1
        order_item.save()
        return render(request, 'rider/success.html')

