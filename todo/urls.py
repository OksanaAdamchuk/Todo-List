from django.urls import include, path

from todo.views import TagCreateView, TagDeleteView, TagListView, TagUpdateView, TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView


urlpatterns = [
    path(
        "", TaskListView.as_view(), name="task-list"
    ),
    path("toggle/<int:pk>/", TaskListView.as_view(), name="toggle-task"),
    path(
        "task/create/", TaskCreateView.as_view(), name="task-create"
    ),
    path(
        "task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "tags/", TagListView.as_view(), name="tag-list"
    ),
    path(
        "tags/create/", TagCreateView.as_view(), name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"
    ),
]

app_name = "todo"