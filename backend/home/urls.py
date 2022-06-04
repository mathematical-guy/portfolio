from home.views import SkillListView, ProjectListView
from django.urls import path


urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]
