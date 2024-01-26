from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProjectListView.as_view(), name="list"),
    path("create/", views.ProjectCreateView.as_view(), name="create"),
    path("<int:project_id>/", views.ProjectDetailView.as_view(), name="detail"),
    path("<int:project_id>/update/", views.ProjectUpdateView.as_view(), name="update"),
    path("<int:project_id>/delete/", views.ProjectDeleteView.as_view(), name="delete"),
    path("<int:project_id>/submit/", views.submit_view, name="submit"),
    path("<int:project_id>/leave/", views.leave_view, name="leave"),
    path("<int:project_id>/kick/<int:user_id>/", views.kick_view, name="kick"),
    path("my_project/", views.my_project_view, name="my_project"),
]
