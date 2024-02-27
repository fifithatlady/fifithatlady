from django.urls import path
from . import views

app_name = 'milestones'

urlpatterns = [
    path('log_milestone/<int:baby_id>/', views.log_milestone, name='log_milestone'),
    path('log_previous_milestone/<int:baby_id>/<int:month>/', views.log_previous_milestone, name='log_previous_milestone'),  # New url for previous months' milestones
    path('view_expected_milestones/<int:baby_id>/', views.view_expected_milestones, name='view_expected_milestones'),
    path('view_activities/<int:baby_id>/', views.view_activities, name='view_activities'),
    path('view_nutrition_guide/<int:baby_id>/', views.view_nutrition_guide, name='view_nutrition_guide'),
]
