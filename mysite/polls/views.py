from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Survey
from .models import Question
from .models import SurveyOptions


def index(request):
    survey_list = Survey.objects.all()
    context = {
        "survey_list": survey_list,
    }
    return render(request, "polls/index.html", context)

from django.http import Http404

def detail(request, survey_id):
    question_list = get_list_or_404(Question, survey=survey_id)
    survey_name = get_object_or_404(Survey, id=survey_id)
    choices = get_list_or_404(SurveyOptions)
    context = {
        "question_list": question_list,
        "survey_name": survey_name,
        "choices": choices,
    }
    return render(request, "polls/detail.html", context)


def results(request, survey_id):
    response = "You're looking at the results of survey %s."
    return HttpResponse(response % survey_id)


def vote(request, survey_id):
    questions = get_list_or_404(Question, pk=survey_id)
    selected_choices = {}
    try:
        for question in questions:
            selected_choice = question.choice_set.get(pk=request.POST[str(question.id)])
            selected_choices[question.id] = selected_choice
    except (KeyError, SurveyOptions.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "questions": questions,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        for question_id, choice in selected_choices.items():
            choice.votes += 1
            choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        print("Redirecting to results page")

        return HttpResponseRedirect(reverse("polls:results", args=(survey_id,)))
# Create your views here.
