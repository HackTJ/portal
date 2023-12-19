from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rules.contrib.views import AutoPermissionRequiredMixin, PermissionRequiredMixin

from .models import Location


class LocationListView(PermissionRequiredMixin, ListView):
    context_object_name = "locations"
    model = Location
    ordering = ["floor", "room"]
    permission_required = "locations.list_location"


class LocationCreateView(AutoPermissionRequiredMixin, CreateView):
    context_object_name = "location"
    extra_context = {"title": "Create Location"}
    fields = ["name", "floor", "room", "capacity"]
    model = Location
    pk_url_kwarg = "location_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("locations:detail", kwargs={"location_id": self.object.id})


class LocationDetailView(AutoPermissionRequiredMixin, DetailView):
    context_object_name = "location"
    model = Location
    pk_url_kwarg = "location_id"


class LocationUpdateView(AutoPermissionRequiredMixin, UpdateView):
    context_object_name = "location"
    extra_context = {"title": "Update Location"}
    fields = ["name", "floor", "room", "capacity"]
    model = Location
    pk_url_kwarg = "location_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("locations:detail", kwargs={"location_id": self.object.id})


class LocationDeleteView(AutoPermissionRequiredMixin, DeleteView):
    context_object_name = "location"
    extra_context = {"title": "Delete Location"}
    model = Location
    pk_url_kwarg = "location_id"
    template_name = "obj_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("locations:list")
