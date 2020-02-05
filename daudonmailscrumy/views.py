import random
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from daudonmailscrumy.models import ScrumyGoals, GoalStatus

def index(request):
    goals = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goals)

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(goal)

def add_goal(request):
    ScrumyGoals.objects.create(
        goal_name = "Keep Learning Django",
        goal_id = _generate_goal_id(),
        created_by = "Louis",
        moved_by = "Louis",
        owner = "Louis",
        goal_status = GoalStatus.objects.get(status_name="Weekly Goal"),
        user = User.objects.get(username="louis")
    )
    return HttpResponse("Goal successfully created")

def home(request):
    scrumy_goals = ScrumyGoals.objects.filter(goal_name="Keep Learning Django")
    scrumy_goal = scrumy_goals[0]
    context = {
        "goal_name":scrumy_goal.goal_name,
        "goal_id":scrumy_goal.goal_id,
        "user":scrumy_goal.user
    }
    return render(request,"daudonmailscrumy/home.html",context)





#helper
def _generate_goal_id():
    goal_id = 0
    while True:
        random_number = random.randint(1000,9999)
        scrumy_goals = ScrumyGoals.objects.filter(goal_id = random_number)
        if not len(scrumy_goals):
            goal_id = random_number
            break
    return goal_id
