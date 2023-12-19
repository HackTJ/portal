from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Location


class LocationListView(ListView):
    context_object_name = "locations"
    model = Location


class LocationCreateView(CreateView):
    context_object_name = "location"
    extra_context = {"title": "Create Location"}
    fields = ["name", "floor", "room", "capacity"]
    model = Location
    pk_url_kwarg = "location_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("locations:detail", kwargs={"location_id": self.object.id})


class LocationDetailView(DetailView):
    context_object_name = "location"
    model = Location
    pk_url_kwarg = "location_id"


class LocationUpdateView(UpdateView):
    context_object_name = "location"
    extra_context = {"title": "Update Location"}
    fields = ["name", "floor", "room", "capacity"]
    model = Location
    pk_url_kwarg = "location_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("locations:detail", kwargs={"location_id": self.object.id})


class LocationDeleteView(DeleteView):
    context_object_name = "location"
    extra_context = {"title": "Delete Location"}
    model = Location
    pk_url_kwarg = "location_id"
    template_name = "obj_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("locations:list")
