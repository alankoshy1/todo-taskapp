from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('class/', views.TaskList.as_view(), name='class'),
    path('detail/<int:pk>/', views.DetailList.as_view(),name='detail'),
    path('update/<int:pk>/', views.UpdateList.as_view(),name='update'),
    path('delete/<int:pk>/', views.DeleteList.as_view(),name='delete'),

]