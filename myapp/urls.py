from django.urls import path
from .views import (HomePageView, WorkspacePageView, BugListView, BugCreateView, ProjectBugListView, ProjectCreateView,
                    BugUpdateView, BugDeleteView, AnnouncementListView, AnnouncementCreateView, AnnouncementUpdateView, AnnouncementDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('workspace/', WorkspacePageView.as_view(), name='workspace'),
    path('projects/<int:pk>/bugs/', ProjectBugListView.as_view(), name='project_bugs'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('bug/list/', BugListView.as_view(), name='bug_list'),
    path('bug/create/', BugCreateView.as_view(), name='bug_create'),
    path('bugs/<int:pk>/update/', BugUpdateView.as_view(), name='bug_update'),
    path('<int:pk>/delete/', BugDeleteView.as_view(), name='bug_delete'),
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcements/create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement/<int:pk>/edit/', AnnouncementUpdateView.as_view(), name='announcement_edit'),
    path('announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement_delete'),





]