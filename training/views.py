from django.shortcuts import get_object_or_404,render
from .models import TrainingQuestion

# Create your views here.
def t_index(request):
    list_trainig = TrainingQuestion.objects.order_by('-date_create_trainig')[:10]
    context = {'list_trainig': list_trainig}
    return render(request, 'training/t_index.html', context)

def t_detail(request, training_id):
    training = get_object_or_404(TrainingQuestion, pk=training_id)
    return render(request, 'training/t_detail.html', {'training': training})