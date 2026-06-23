from django.shortcuts import render, redirect
from config.firebase import db
from django.contrib.auth.decorators import login_required
from accounts.decorators import module_access

@module_access('inventory')
def index(request):
    if request.method == 'POST':
        data = {
            'item_name': request.POST.get('item_name'),
            'sku': request.POST.get('sku'),
            'category': request.POST.get('category'),
            'quantity': int(request.POST.get('quantity', 0)),
            'unit_price': float(request.POST.get('unit_price', 0.0))
        }
        db.collection('products').add(data)
        return redirect('inventory:index')

    docs = db.collection('products').stream()
    products = []
    for doc in docs:
        prod = doc.to_dict()
        prod['id'] = doc.id
        products.append(prod)

    return render(request, 'inventory/index.html', {'products': products})
