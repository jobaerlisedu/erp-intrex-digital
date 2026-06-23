from django.shortcuts import render, redirect
from config.firebase import db
from django.contrib.auth.decorators import login_required
from accounts.decorators import module_access

@module_access('billing')
def index(request):
    if request.method == 'POST':
        data = {
            'client_name': request.POST.get('client_name'),
            'invoice_number': request.POST.get('invoice_number'),
            'amount': float(request.POST.get('amount', 0.0)),
            'due_date': request.POST.get('due_date'),
            'status': request.POST.get('status', 'Pending')
        }
        db.collection('invoices').add(data)
        return redirect('billing:index')

    docs = db.collection('invoices').stream()
    invoices = []
    for doc in docs:
        inv = doc.to_dict()
        inv['id'] = doc.id
        invoices.append(inv)

    return render(request, 'billing/index.html', {'invoices': invoices})
