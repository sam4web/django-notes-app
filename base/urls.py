from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("add/", add_note, name="add-note"),
    path("delete/<str:pk>", delete_note, name="delete-note"),
    path("edit/<str:pk>", edit_note, name="edit-note"),
    path("display/<str:pk>/", display_note, name="display-note"),
]
