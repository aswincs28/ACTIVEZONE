from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    report_type = models.CharField(max_length=50)
    data = models.JSONField()  # Store analytics data
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} - {self.generated_at}"

class SystemLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='admin_logs')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"

class Dispute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_disputes')
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('open', 'Open'), ('resolved', 'Resolved')],
        default='open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispute by {self.user.username} - {self.status}"
    # turf/models.py

class Turf(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=False)  # <-- new field

    def __str__(self):
        return self.name

