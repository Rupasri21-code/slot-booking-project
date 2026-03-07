from django.shortcuts import render, redirect
from .models import Slot

def home(request):
    slots = Slot.objects.all()
    return render(request, 'home.html', {'slots': slots})

def book_slot(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    slot.is_booked = True
    slot.save()
    return redirect('home')

def unbook_slot(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    slot.is_booked = False
    slot.save()
    return redirect('home')