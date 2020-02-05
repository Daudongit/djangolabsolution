from django.shortcuts import render
from django.http import HttpResponse
from daudonmailscrumy.models import ScrumyGoals

def index(request):
    goals = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goals)