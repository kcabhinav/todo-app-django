from django.shortcuts import get_object_or_404, render, redirect
from django.utils.cache import HttpResponse
from .forms import TodoForm
from .models import Todo


# Create your views here.

def task_list(request) -> HttpResponse:
    ctx = {'todo_list': Todo.objects.all()}
    return render(request, 'main/list.html', ctx)

def todo_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TodoForm()
        else:
            task = Todo.objects.get(id=id)
            form = TodoForm(instance=task)

        return render(request, 'main/task.html', {'form': form})

    else:
        if id == 0:
            form = TodoForm(request.POST)
        else:
            task = Todo.objects.get(id=id)
            form = TodoForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
        return redirect(task_list)

def delete_task(request, id=0):
    task = Todo.objects.get(id=id)
    # task = get_object_or_404(Todo, id)
    if request.method != "POST":
        return redirect(task_list)
    task.delete()
    return redirect(task_list)
