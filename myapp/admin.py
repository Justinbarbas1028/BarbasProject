from django.contrib import admin
from .models import  Project, Bug, BugHistory, Comment
# Register your models here.
admin.site.register(Project)
admin.site.register(Bug)
admin.site.register(BugHistory)
admin.site.register(Comment)
