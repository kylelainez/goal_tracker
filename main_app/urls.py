from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/signup/', views.signup, name='signup'),
    path('goals/', views.goals_index, name="index"),
    path('user/<int:user_id>/goals/', views.user_goals, name="user_goals"),
    path('user/<int:user_id>/goals/<int:pk>/', views.GoalListDetails.as_view(), name="detail"),
    path('user/<int:user_id>/goals/create', views.CreateList.as_view(), name="create_goallist"),
    path('user/<int:user_id>/goals/<int:list_id>/add_goal', views.add_goal, name="add_goal"),
]
