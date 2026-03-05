from django.shortcuts import render, redirect
from .models import Slot

def view_slots(request):
    slots = Slot.objects.all()
    return render(request, 'slots.html', {'slots': slots})

def book_slot(request, id):
    slot = Slot.objects.get(id=id)
    slot.is_booked = True
    slot.save()
    return redirect('/')