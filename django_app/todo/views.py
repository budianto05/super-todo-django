from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.utils.dateparse import parse_datetime

# READ + CREATE
def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority', 'M')
        due_date_str = request.POST.get('due_date')

        # parse string to datetime safely
        due_date = parse_datetime(due_date_str) if due_date_str else None

        Todo.objects.create(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )

        return redirect('todo_list')

    todos = Todo.objects.all().order_by(
        'is_completed',
        '-priority',
        'due_date'
    )

    return render(
        request,
        'todo/todo_list.html',
        {'todos': todos}
    )

# UPDATE / TOGGLE
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todo_list')

# DELETE
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
