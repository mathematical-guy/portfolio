from django.shortcuts import render
from home.models import Skill, Project
from rest_framework.generics import ListAPIView
from home.serializers import SkillSerializers, ProjectSerializer


class SkillListView(ListAPIView):
    serializer_class = SkillSerializers
    queryset = Skill.objects.all()


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
