from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_task/", views.add_task, name="add_task"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("toggle_task/<int:task_id>/", views.toggle_task, name="toggle_task"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/add/", views.add_tag, name="add_tag"),
    path("tags/edit/<int:pk>/", views.edit_tag, name="edit_tag"),
    path("tags/delete/<int:tag_id>/", views.delete_tag, name="delete_tag"),
]
