from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Category


class CategoryListView(ListView):
    context_object_name = "categories"
    model = Category


class CategoryCreateView(CreateView):
    context_object_name = "category"
    extra_context = {"title": "Create Category"}
    fields = ["name", "description"]
    model = Category
    pk_url_kwarg = "category_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("categories:detail", kwargs={"category_id": self.object.id})


class CategoryDetailView(DetailView):
    context_object_name = "category"
    model = Category
    pk_url_kwarg = "category_id"


class CategoryUpdateView(UpdateView):
    context_object_name = "category"
    extra_context = {"title": "Update Category"}
    fields = ["name", "description"]
    model = Category
    pk_url_kwarg = "category_id"
    template_name = "obj_form.html"

    def get_success_url(self):
        return reverse_lazy("categories:detail", kwargs={"category_id": self.object.id})


class CategoryDeleteView(DeleteView):
    context_object_name = "category"
    extra_context = {"title": "Delete Category"}
    model = Category
    pk_url_kwarg = "category_id"
    template_name = "obj_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("categories:list")
