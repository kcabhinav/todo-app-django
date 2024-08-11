from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('form_add', views.todo_form, name='task_add'),
    path('<int:id>/edit', views.todo_form, name='task_edit'),
    path('<int:id>/delete', views.delete_task, name = 'task_delete')
]
