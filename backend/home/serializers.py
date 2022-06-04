from home.models import Skill, Project
from rest_framework import serializers


class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'strength')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("name", "description", "year", "is_personal")
