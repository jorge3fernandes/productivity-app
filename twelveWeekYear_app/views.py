from django.shortcuts import render, redirect
from .models import *
from .forms import GoalForm, TacticForm, TwelveWeekForm
from utilities import *

# Create your views here.

def index(request):
    goals = Goal.objects.all()
    tactics = Tactic.objects.all()
    '''
    When creating records, make sure they cascade through
    exemple:
        if creating new tactic, make sure it also creates a record in the DailyScore model.
            together with the date when it is due. if daily we create a record for each day, weekly, 
            each week, if none we inherit the date.
        When creating a 12 week, automatic create all the weeks
    '''
    context = {"goals": goals,
               "tactics": tactics}
    return render(request, "twelveWeekYear_app/index.html", context)


def create_12week_session(request):
    if request.method == 'POST':
        form_set = TwelveWeekForm(request.POST)
        if form_set.is_valid():
            session_instance = form_set.save(commit=False)
            start_date = form_set.cleaned_data.get("start_date")

            week1_start_date = getWeek(start_date)[0]
            week12_end_date = week1_start_date + timedelta(days = 83)
            session_days = generateDays(week1_start_date, week12_end_date, 'd')

            # creating all the weeks in the session
            n = 7
            week_number = 1
            session_instance.save()
            for i in range(0, len(session_days), n):
                week_instance = Week(twelve_week=session_instance, title=f"week {week_number}",
                                    start_date=session_days[i:i+n][0], end_date=session_days[i:i+n][-1])
                week_number += 1
                week_instance.save()
                for day in session_days[i:i+n]:
                    day_instance = DailyReflection(week=week_instance, date=day)
                    day_instance.save()
            # creating all the days in the session


            print("Session Created!")

            redirect("index") 
        else:
            print("form error")

    session_form = TwelveWeekForm()
    context = {"session_form": session_form}
    return render(request, "twelveWeekYear_app/add_session.html", context)

def add_goal(request):
    print(request.method)
    if request.method == 'POST':
        form_set = GoalForm(request.POST)
        if form_set.is_valid():
            form_set.save()
            print("Goal saved!")

            redirect("/")
        else:
            print("form error")


    goal_form = GoalForm()
    context = {"goal_form": goal_form}
    return render(request, "twelveWeekYear_app/add_goal.html", context)


def add_tactic(request):
    print(request.method)
    if request.method == 'POST':
        form_set = TacticForm(request.POST)
        if form_set.is_valid():
            form_set.save()
            '''
            Add tactic to day based on start/due date, daily, once
            '''
            print("Goal saved!")

            redirect("/")
        else:
            print("form error")

    tactic_form = TacticForm()
    context = {"tactic_form": tactic_form}
    return render(request, "twelveWeekYear_app/add_tactic.html", context)



