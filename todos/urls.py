from django.urls import path
from .views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
]

# 📂 Edite o arquivo: setup/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todos.urls")),  # Conecta as URLs do app
]