from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag

