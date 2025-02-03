from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = SignUpForm()
    return render(request, 'todos/signup.html', {'form': form})

class IndexView(LoginRequiredMixin, generic.ListView):
    
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return todos for the logged-in user, ordered by creation time."""
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title, user=request.user)
        return redirect('todos:index')
    return render(request, 'todos/add.html')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')