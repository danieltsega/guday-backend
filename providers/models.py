from django.db import models

class Provider(models.Model):
    id = models.AutoField(primary_key=True)  # Unique identifier for each provider
    name = models.TextField()  # Full name of the provider
    contact_number = models.TextField()  # Phone number to reach the provider
    email = models.TextField()  # Email address of the provider
    tasks_offered = models.TextField()  # List or summary of tasks the provider can help with
    location = models.TextField()  # City or area where the provider operates
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the provider was created

    def __str__(self):
        return self.name

