from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='roomIndex'),
    path('create', views.create, name='roomCreate'),
    path('<int:room_id>', views.waitingRoom, name='waitingRoom'),
    path('status', views.status, name='roomStatus'),
    path('update', views.update, name='roomUpdate'),
]