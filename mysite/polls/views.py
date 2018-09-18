from django.shortcuts import get_object_or_404, render
from django.template import loader

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = { "latest_question_list" : latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": q})

    # return HttpResponse("You're looking at question {}.".format(question_id))


def results(request, question_id):
    # response = "You're looking at the results of question {}."
    # return HttpResponse(response.format(question_id))
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question {}.".format(question_id))
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))