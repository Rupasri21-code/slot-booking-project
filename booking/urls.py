from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_slots, name='view_slots'),
    path('book/<int:id>/', views.book_slot, name='book_slot'),
]