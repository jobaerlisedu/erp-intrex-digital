from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('requisitions/', views.requisitions_list, name='requisitions_list'),
    path('vendors/', views.vendors_list, name='vendors_list'),
    path('rfq/', views.rfq_list, name='rfq_list'),
    path('po/', views.po_list, name='po_list'),
    path('grn/', views.grn_list, name='grn_list'),
    path('stock/', views.stock_list, name='stock_list'),
    path('deliveries/', views.delivery_list, name='delivery_list'),
]
