from django.urls import path
from . import views
urlpatterns = [
    path('addTask/',views.addTask,name="addTask"),
    path('markAsRead/<int:pk>/',views.markAsRead,name="markAsRead"),
    path('markAsUnRead/<int:pk>/',views.markAsUnRead,name="markAsUnRead"),
    path('editTask/<int:pk>/',views.editTask,name="editTask"),
    path('deleteTask/<int:pk>/',views.deleteTask,name='deleteTask'),
]