from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.tasks_list, name='list'),
    path("create/", views.task_create, name="create"),
    path("add-task/", views.add_task, name="api-add-task"),
    path('complete/<int:uid>', views.complete_task, name='complete'),
    path('delete/<int:uid>', views.delete_task, name='delete'),
    path("export/", views.TaskExportView.as_view(), name="export"),
]
  #path("complete/", views.TaskCompleteView.as_view(), name="complete"),