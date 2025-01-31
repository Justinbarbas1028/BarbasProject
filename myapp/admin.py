from django.contrib import admin
from .models import  Project, Bug, BugHistory, Comment, Announcement
# Register your models here.
admin.site.register(Project)
admin.site.register(Bug)
admin.site.register(BugHistory)
admin.site.register(Comment)
admin.site.register(Announcement)
