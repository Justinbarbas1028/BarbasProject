from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Bug, Project, Announcement
from .forms import BugForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'myapp/homepage.html'


class WorkspacePageView(ListView):
    model = Project
    template_name = 'myapp/workspace.html'
    context_object_name = 'projects'


class ProjectBugListView(ListView):
    model = Bug
    template_name = 'myapp/bug_list.html'
    context_object_name = 'bugs'

    def get_queryset(self):
        project_id = self.kwargs['pk']
        return Bug.objects.filter(project_id=project_id)


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'members']
    template_name = 'myapp/project_form.html'
    success_url = reverse_lazy('workspace')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BugListView(ListView):
    model = Bug
    template_name = 'myapp/bug_list.html'
    context_object_name = 'bugs'
    ordering = ['-priority']

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', self.ordering)
        return ordering


class BugCreateView(CreateView):
    model = Bug
    fields = ['title', 'description', 'status', 'priority', 'severity', 'project', 'assigned_to']
    template_name = 'myapp/bug_form.html'
    success_url = reverse_lazy('workspace')

    def form_valid(self, form):
        form.instance.reported_by = self.request.user
        return super().form_valid(form)


class BugUpdateView(UpdateView):
    model = Bug
    form_class = BugForm
    template_name = 'myapp/bug_update.html'
    context_object_name = 'bug'

    def get_success_url(self):
        return reverse_lazy('bug_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(reported_by=user) | queryset.filter(assigned_to=user)
        return queryset

    def get_initial(self):
        initial = super().get_initial()
        bug = self.get_object()
        return initial


class BugDeleteView(DeleteView):
    model = Bug
    template_name = 'myapp/bug_confirm_delete.html'
    success_url = reverse_lazy('bug_list')

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'myapp/Announcement.html'
    context_object_name = 'announcements'
    ordering = ['-created_at']

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_at')
        return ordering


class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'content']
    template_name = 'myapp/Announcement_form.html'
    success_url = reverse_lazy('announcement_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['title', 'content']
    template_name = 'myapp/Announcement_update.html'
    success_url = reverse_lazy('announcement_list')


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'myapp/announcement_confirm_delete.html'
    success_url = reverse_lazy('announcement_list')
