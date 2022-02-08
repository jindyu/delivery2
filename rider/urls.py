from django.urls import path, include
from rider import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
]
