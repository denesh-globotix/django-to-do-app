from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem

# Create your views here.
def todoView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {
        'all_items': all_todo_items
    })

def addTODO(request):
    x = request.POST['name']
    print(x)
    new_item = TodoListItem(name=x)
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/')