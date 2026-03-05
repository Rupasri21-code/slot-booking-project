from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_slots, name='view_slots'),
    path('toggle_ajax/<int:id>/', views.toggle_slot_ajax, name='toggle_slot_ajax'),
]