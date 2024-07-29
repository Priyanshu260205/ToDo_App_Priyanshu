from django.shortcuts import render, redirect

from .models import Mytodo

# =================================== VIEWS HERE =========================

def home(request):    
    return render(request, "home.html")

# ====================================== TODO =========================================

def todo(request):
    
    todos = Mytodo.objects.filter(is_completed = False)
    
    parameters = {
        "todos": todos, # isme koi bhi completed todo nhi h
    }
    
    return render(request, "todo.html", parameters) # isme jo parameter ja rha h usme bhi koi completed todo nhi h


# ===================================== ADD TODO =======================================

def add_todo(request):
    
    if request.method == "POST":
        
        # Template s view m data la rha hu
        user_task = request.POST.get("task")
        user_due_at = request.POST.get("due_at")
        
        # View vala data model m save kr rha hu
        new_todo = Mytodo(
            task = user_task, 
            due_at = user_due_at,
            is_completed = False
            )
        new_todo.save()
        
        return redirect("todo")
        
    return render(request, "add_todo.html")



#============================================ DELETE TODO ===============================================================

def delete_todo(request, todo_id):
    
    todo = Mytodo.objects.get(id = todo_id)
    todo.delete()
    
    return redirect("todo")


#==========================================UPDATE TODO ==================================================================

def update_todo(request, todo_id):
    
    todo = Mytodo.objects.get(id= todo_id)
    
    if request.method == "POST":
        
        user_task = request.POST.get("task")
        user_due_at = request.POST.get("due_at")
        
        todo.task = user_task
        todo.due_at = user_due_at
        
        todo.save()
        
        return redirect("todo")
    
    parameters = {
        "todo" : todo
    }
    
    return render(request,"update_todo.html",parameters)


#=========================================== MARK COMPLETE ==============================================================

def mark_complete(request, todo_id):
    todo = Mytodo.objects.get(id = todo_id)
    
    todo.is_completed = True
    todo.save()
    
    return redirect("todo")