from django.db import models

class Slot(models.Model):
    time = models.CharField(max_length=20)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.time