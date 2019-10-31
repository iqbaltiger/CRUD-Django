from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TodoForm
from .models import Todo
from django.utils import timezone


# Create your views here.


def index(request):

    todoList = Todo.objects.all().order_by('-date')

    return render(request, 'todo/list.html', {'list': todoList})


def saveAction(request):
    print(request.POST)
    todoform = TodoForm(request.POST or None)

    if todoform.is_valid():
        todoform.save()

        return redirect('/')
    return render(request, 'todo/index.html', {'form': todoform})


def editTodo(request, pk):

    pickTodo = Todo.objects.get(pk=pk)

    editForm = TodoForm(request.POST or None, instance=pickTodo)

    if editForm.is_valid():
        editForm.save()
        return redirect('/')

    return render(request, 'todo/index.html', {'form': editForm})


def deleteAction(request, pk):

    pickTodo = Todo.objects.get(pk=pk)
    pickTodo.delete()

    return redirect('/')
