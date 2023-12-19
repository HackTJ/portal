from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rules.contrib.views import AutoPermissionRequiredMixin, PermissionRequiredMixin

from .models import Project


class ProjectListView(PermissionRequiredMixin, ListView):
    context_object_name = "projects"
    model = Project
    ordering = ["-created_at"]
    permission_required = "projects.list_project"


class ProjectCreateView(AutoPermissionRequiredMixin, CreateView):
    context_object_name = "project"
    extra_context = {"title": "Create Project"}
    fields = ["name", "description", "categories", "location", "location_description"]
    model = Project
    pk_url_kwarg = "project_id"
    template_name = "obj_form.html"

    def form_valid(self, form):
        return_value = super().form_valid(form)

        self.object.created_by = self.request.user
        self.object.last_modified_by = self.request.user
        self.object.members.add(self.request.user)
        self.object.save()

        return return_value

    def get_success_url(self):
        return reverse_lazy("projects:detail", kwargs={"project_id": self.object.id})


class ProjectDetailView(AutoPermissionRequiredMixin, DetailView):
    context_object_name = "project"
    model = Project
    pk_url_kwarg = "project_id"


class ProjectUpdateView(AutoPermissionRequiredMixin, UpdateView):
    context_object_name = "project"
    extra_context = {"title": "Update Project"}
    fields = ["name", "description", "categories", "location", "location_description"]
    model = Project
    pk_url_kwarg = "project_id"
    template_name = "obj_form.html"

    def form_valid(self, form):
        return_value = super().form_valid(form)

        self.object.last_modified_by = self.request.user
        self.object.save()

        return return_value

    def get_success_url(self):
        return reverse_lazy("projects:detail", kwargs={"project_id": self.object.id})


class ProjectDeleteView(AutoPermissionRequiredMixin, DeleteView):
    context_object_name = "project"
    extra_context = {"title": "Delete Project"}
    model = Project
    pk_url_kwarg = "project_id"
    template_name = "obj_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("projects:list")


def my_project_view(request: HttpRequest) -> HttpResponse:
    projects = request.user.projects

    if not projects.exists():
        return redirect("projects:create")

    project = projects.first()
    return redirect("projects:detail", project.id)
