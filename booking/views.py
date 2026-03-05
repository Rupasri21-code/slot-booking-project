from django.shortcuts import render
from django.http import JsonResponse
from .models import Slot

# Display all slots
def view_slots(request):
    slots = Slot.objects.all()
    return render(request, 'slots.html', {'slots': slots})

# Toggle booking/unbooking via AJAX
def toggle_slot_ajax(request, id):
    try:
        slot = Slot.objects.get(id=id)
        slot.is_booked = not slot.is_booked
        slot.save()
        return JsonResponse({'is_booked': slot.is_booked})
    except Slot.DoesNotExist:
        return JsonResponse({'error': 'Slot not found'}, status=404)