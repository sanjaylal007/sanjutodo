from . import views
from django.urls import path


app_name='todoapp'

urlpatterns = [
    path('',views.task,name='task'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvedit/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvedit'),
    path('cbvdelete/<int:pk>/',views.TaskDeletelview.as_view(),name='cbvdelete')

]

