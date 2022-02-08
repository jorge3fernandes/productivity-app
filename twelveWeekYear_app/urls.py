from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_goal', views.add_goal, name='add_goal'),
    path('add_tactic', views.add_tactic, name='add_tactic'),
    path('add_session', views.create_12week_session, name='add_session')
]