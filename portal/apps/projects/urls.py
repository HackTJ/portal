from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProjectListView.as_view(), name="list"),
    path("create/", views.ProjectCreateView.as_view(), name="create"),
    path("<int:project_id>/", views.ProjectDetailView.as_view(), name="detail"),
    path("<int:project_id>/update/", views.ProjectUpdateView.as_view(), name="update"),
    path("<int:project_id>/delete/", views.ProjectDeleteView.as_view(), name="delete"),
    path("my_project/", views.my_project_view, name="my_project"),
]
