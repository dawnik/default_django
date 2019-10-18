from django.shortcuts import get_object_or_404, render
from .models import TreiningTopic
def index(request):
    return render(request, 'default_page/index.html')

def showall(request):
    subjects_trenig = TreiningTopic
    context = {'subjects_trenig': subjects_trenig}
    return render(request, 'default_page/detail.html', context)

def detail(request, subject_id):
    subjects = get_object_or_404(TreiningTopic, pk=subject_id)
    return render(request, 'default_page/detail.html', {'subjects': subjects})