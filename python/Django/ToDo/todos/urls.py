from django.urls import path
from . import views

urlpatterns = [

    # Add Task
    path('addtask/', views.addTask, name='addTask'),

    # Mark as done feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # Mark as undone feature 
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    # Edit features 
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
        # Delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]