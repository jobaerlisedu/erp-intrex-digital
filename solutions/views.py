from django.shortcuts import render, redirect
from config.firebase import db
from django.contrib.auth.decorators import login_required
from accounts.decorators import module_access

@module_access('solutions')
def index(request):
    if request.method == 'POST':
        data = {
            'client_name': request.POST.get('client_name'),
            'service_type': request.POST.get('service_type'),
            'priority': request.POST.get('priority'),
            'status': request.POST.get('status', 'Open')
        }
        db.collection('service_tickets').add(data)
        return redirect('solutions:index')

    docs = db.collection('service_tickets').stream()
    tickets = []
    for doc in docs:
        ticket = doc.to_dict()
        ticket['id'] = doc.id
        tickets.append(ticket)

    return render(request, 'solutions/index.html', {'tickets': tickets})
