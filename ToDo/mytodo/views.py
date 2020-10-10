from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'mytodo/index.html', content)
    # return HttpResponse("<h1>hello</h1>")

def createTodo(request):
    user_input_str = request.POST['todoContent']
    
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    #return HttpResponse("저장했습니다 =>")
    return HttpResponseRedirect(reverse("index"))


# def doneTodo(request):
#     done_todo_id = request.GET['todoNum']
#     print("완료한 todo의 id",done_todo_id)
#     todo = Todo.objects.get(id = done_todo_id)
#     todo.isDone = True
#     todo.save()
#     return HttpResponseRedirect(reverse("index"))