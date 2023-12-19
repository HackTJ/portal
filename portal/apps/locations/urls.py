from django.urls import path

from . import views


urlpatterns = [
    path("", views.LocationListView.as_view(), name="list"),
    path("create/", views.LocationCreateView.as_view(), name="create"),
    path("<int:location_id>/", views.LocationDetailView.as_view(), name="detail"),
    path("<int:location_id>/update/", views.LocationUpdateView.as_view(), name="update"),
    path("<int:location_id>/delete/", views.LocationDeleteView.as_view(), name="delete"),
]
