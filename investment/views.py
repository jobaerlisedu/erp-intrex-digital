from django.shortcuts import render, redirect
from config.firebase import db
from django.contrib.auth.decorators import login_required
from accounts.decorators import module_access

@module_access('investment')
def index(request):
    if request.method == 'POST':
        data = {
            'asset_name': request.POST.get('asset_name'),
            'asset_class': request.POST.get('asset_class'),
            'invested_amount': float(request.POST.get('invested_amount', 0.0)),
            'current_value': float(request.POST.get('current_value', 0.0))
        }
        db.collection('portfolios').add(data)
        return redirect('investment:index')

    docs = db.collection('portfolios').stream()
    portfolios = []
    for doc in docs:
        port = doc.to_dict()
        port['id'] = doc.id
        port['roi'] = round(((port.get('current_value', 0) - port.get('invested_amount', 0)) / (port.get('invested_amount', 1) or 1)) * 100, 2)
        portfolios.append(port)

    return render(request, 'investment/index.html', {'portfolios': portfolios})
