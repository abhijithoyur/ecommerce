from django.contrib import admin
from .import views
from django.urls import path, include

urlpatterns = [
    path('',views.task,name='task'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('chome/',views.List_view.as_view(),name='chome'),
    path('cdetail/<int:pk>/',views.TaskDetail_view.as_view(),name='cdetail'),
    path('cupdate/<int:pk>/',views.TaskUpdate_view.as_view(),name='cupdate'),
    path('cdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cdelete')

]
