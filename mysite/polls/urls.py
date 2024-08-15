from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:survey_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:survey_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:survey_id>/vote/", views.vote, name="vote"),
]