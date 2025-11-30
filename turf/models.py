from django.db import models
# Removed import of ArrayField, as it's not needed anymore.

# Original Time Model (Moved to the top to resolve NameError)
class Time(models.Model):
    name = models.CharField(max_length=200, default="")
    week = models.TextField()  # Changed ArrayField to TextField

    def __str__(self):
        return self.name


# Original Contact Model
class Contact(models.Model):
    yourName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobilenumber = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.yourName


# Original TurfBooking Model
class turfBooking(models.Model):
    time_slot = models.CharField(max_length=12)
    isBooked = models.BooleanField(default=False)
    days = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.time_slot


# Modified bookslot Model with ForeignKey Relationship to turfBooking and Time
class bookslot(models.Model):
    week = models.TextField()  # Changed ArrayField to TextField
    turf_booking = models.ForeignKey(
        turfBooking, on_delete=models.CASCADE, related_name='bookslots', null=True, blank=True
    )
    time = models.ForeignKey(
        Time, on_delete=models.CASCADE, related_name='bookslots', null=True, blank=True
    )

    def __str__(self):
        return f"Bookslot for {self.turf_booking} at {self.time}"


# Original TurfBooked Model
class TurfBooked(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    amount = models.IntegerField()
    selected_date = models.CharField(max_length=200)
    current_date = models.CharField(max_length=200)
    booking_time = models.CharField(max_length=200, default="")
    slots = models.TextField()  # Changed ArrayField to TextField
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
