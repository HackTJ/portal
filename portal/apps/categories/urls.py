from django.urls import path

from . import views


urlpatterns = [
    path("", views.CategoryListView.as_view(), name="list"),
    path("create/", views.CategoryCreateView.as_view(), name="create"),
    path("<int:category_id>/", views.CategoryDetailView.as_view(), name="detail"),
    path("<int:category_id>/update/", views.CategoryUpdateView.as_view(), name="update"),
    path("<int:category_id>/delete/", views.CategoryDeleteView.as_view(), name="delete"),
]
