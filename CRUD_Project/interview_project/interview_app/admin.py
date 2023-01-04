from django.contrib import admin
from .models import InterviewSession
# Register your models here.

@admin.register(InterviewSession)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','designation']
