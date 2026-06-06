from django.shortcuts import render, redirect, get_object_address, get_object_or_404
from .models import Todo
from django.utils import timezone

def todo_list(request):
    # create/tulis
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority', 'M')
        due_date = request.POST.get('due_date')
        
        Todo.objects.create(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date if due_date else None
        )

        return redirect('todo_list')
    # read/baca
    todo = Todo_objects.all().order_by('is_completed', '-priority', 'due_date')
    return render(request, 'todo/todo_list.html', {'todos': todos})

# update/edit
def todo_toggel(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todo_list')

# delete/hapus
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
