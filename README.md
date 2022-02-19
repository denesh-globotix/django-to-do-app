# django-to-do-app
An introduction into the forays of django

## Play by play instructions: 

1. Create a new project
```python
django-admin startproject todo
```
2. Start the server
```sh
cd todo && python3 manage.py runserver 

```
3. Create a new application within the project 
```python
python3 manage.py startapp todoapp
```
4. Register the new application
```python
installed_apps = [
    ...,
    todoapp,
    ...,
]
```
5. Create the template 
```sh 
mkdir templates
cd templates && touch todolist.html
```
6. Add boiler play html 
```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    Hey look everyone, i am learning how to code!
</body>
</html>
```
7. add a view to views.py
```python
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .models import TodoListItem

# Create your views here.
def todoView(request):
    # all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {
        # 'all_items': all_todo_items
    })
```
8. add the url to urls.py in the main app
```python
from django.contrib import admin
from django.urls import path
from todoapp.views import todoView#, addTODO, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todoView),
    # path('addTODO/', addTODO),
    # path('deleteTodoItem/<int:i>/', deleteTodoView),
]
```
9. add the templates to the base directory
```python

import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

10. remove /todo from the endpoint in urls.py
```python
from django.contrib import admin
from django.urls import path
from todoapp.views import todoView#, addTODO, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoView),
    # path('addTODO/', addTODO),
    # path('deleteTodoItem/<int:i>/', deleteTodoView),
]

```
11. create a model in models.py in the app (without the __str__)
```python
from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    name = models.TextField()
```
12. makemigrations
```sh
python3 manage.py makemigrations
```
13. migrate
```python3
python3 manage.py migrate
```
14. Go to localhost:8000 and you will reallise you don't have the username and password. So create a superuser to see the model. 
```sh
python3 manage.py createsuperuser
```
15. register the model in admin
```python
from django.contrib import admin

# Register your models here.
from .models import TodoListItem
admin.site.register(TodoListItem)
```

16. add the __str__ method
```python
class TodoListItem(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
```

17. Add the adding method
    - Add this into todolist.html
        ```html
        <form action="/addTODO/" method="post">
            {% csrf_token %}
            <input type="text" name="name">
            <input type="submit" value="Add Item">
        </form>
        ```
    - Add the url 
        ```python
        path('addTODO/', addTODO),
        ```
    - Add the view
        ```python
        def addTODO(request):
            x = request.POST['name']
            print(x)
            new_item = TodoListItem(name=x)
            new_item.save()
            return HttpResponseRedirect('/')
        ```

18. Add the viewing of the list by commenting out the stuff from before
```python
    def todoView(request):
        all_todo_items = TodoListItem.objects.all()
        return render(request, 'todolist.html', {
            'all_items': all_todo_items
        })
```
19. Add the deleting method
    - Add the html 
    ```html
    <ul>
        {% for i in all_items %}
        <li>
            {{i.name}}
            <form action="/deleteTodoItem/{{i.id}}/" method="post">{% csrf_token %}
                <input type="submit" value="Delete">
            </form>
        </li>
        {% endfor %}
    </ul>
    ```
    - Add the url 
    ```python
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    ```
    - Add the view 
    ```python
    def deleteTodoView(request, i):
        y = TodoListItem.objects.get(id=i)
        y.delete()
        return HttpResponseRedirect('/')
    ```
20. Resource: https://pythonistaplanet.com/to-do-list-app-using-django/
