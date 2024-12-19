from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_tasks = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_tasks': todo_tasks, 'form': form}
    return render(request, 'index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    # print(request.POST['text']) # testing if the data in the form is properly captured

    # Capture data from the text field after the form is submitted
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

# Function to handle completed items in the to-do list
def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

# Delete the tasks that are marked as completed
def deletecompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')

# Delete all tasks
def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')
