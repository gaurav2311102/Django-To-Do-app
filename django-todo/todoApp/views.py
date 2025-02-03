from django.shortcuts import render, redirect

def home(request):
    
    if request.user.is_authenticated: 
        return redirect('todos:index')  # Redirect logged-in users to the todo list
    
    return render(request, 'todos/home.html')  # Render home.html for visitors
