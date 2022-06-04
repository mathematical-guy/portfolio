from django.contrib import admin
from home.models import Skill, Project


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'strength')
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'year', 'is_personal')
    list_filter = ('is_personal', 'year')
    search_fields = ('name',)
