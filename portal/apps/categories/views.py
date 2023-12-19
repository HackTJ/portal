from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rules.contrib.views import AutoPermissionRequiredMixin, PermissionRequiredMixin

from .models import Category


class CategoryListView(PermissionRequiredMixin, ListView):
    context_object_name = "categories"
    model = Category
    ordering = ["name"]
    permission_required = "categories.list_category"


class CategoryCreateView(AutoPermissionRequiredMixin, CreateView):
    context_object_name = "category"
    extra_context = {"title": "Create Category"}
    fields = ["name", "description"]
    model = Category
    pk_url_kwarg = "category_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("categories:detail", kwargs={"category_id": self.object.id})


class CategoryDetailView(AutoPermissionRequiredMixin, DetailView):
    context_object_name = "category"
    model = Category
    pk_url_kwarg = "category_id"


class CategoryUpdateView(AutoPermissionRequiredMixin, UpdateView):
    context_object_name = "category"
    extra_context = {"title": "Update Category"}
    fields = ["name", "description"]
    model = Category
    pk_url_kwarg = "category_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("categories:detail", kwargs={"category_id": self.object.id})


class CategoryDeleteView(AutoPermissionRequiredMixin, DeleteView):
    context_object_name = "category"
    extra_context = {"title": "Delete Category"}
    model = Category
    pk_url_kwarg = "category_id"
    template_name = "obj_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("categories:list")
