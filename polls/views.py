from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question
from django.http import Http404
from django.template import loader



def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/question_id.html", {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index_question(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    # template = loader.get_template('polls/polls_index.html')
    context_question = {
        'latest_question_list': latest_question_list
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context_question, request))
    return render(request, 'polls/index_question.html', context_question)