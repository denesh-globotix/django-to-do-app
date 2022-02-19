from django.contrib import admin

# Register your models here.
from .models import TodoListItem
admin.site.register(TodoListItem)