from django.shortcuts import render, redirect
from config.firebase import db
from django.contrib.auth.decorators import login_required
from accounts.decorators import module_access

@module_access('training')
def index(request):
    if request.method == 'POST':
        data = {
            'course_title': request.POST.get('course_title'),
            'instructor': request.POST.get('instructor'),
            'capacity': int(request.POST.get('capacity', 0)),
            'enrolled': int(request.POST.get('enrolled', 0))
        }
        db.collection('courses').add(data)
        return redirect('training:index')

    docs = db.collection('courses').stream()
    courses = []
    for doc in docs:
        course = doc.to_dict()
        course['id'] = doc.id
        courses.append(course)

    return render(request, 'training/index.html', {'courses': courses})
