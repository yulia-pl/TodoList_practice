from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Tag
from .forms import TaskForm, TagForm


# Home page - list tasks
def home(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "home.html", {"tasks": tasks})


# Add task page
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "add_task.html", {"form": form})


# Edit task page
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(request, "edit_task.html", {"form": form, "task": task})


# Delete task page
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("home")


# Toggle task completion status
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return redirect("home")


# Tag list page
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tag_list.html", {"tags": tags})


# Add tag page
def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm()
    return render(request, "add_tag.html", {"form": form})


# Edit tag page
def edit_tag(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("tag_list")
    else:
        form = TagForm(instance=tag)
    return render(request, "edit_tag.html", {"form": form, "tag": tag})


# Delete tag page
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return redirect("tag_list")
