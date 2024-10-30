from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('private', 'Private'),
        ('government', 'Government'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()  # This will include steps, estimated time, and location
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)  # Choices for task category
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the task was last updated

    def __str__(self):
        return self.title

