from django.db import models
from users.models import User

class Task(models.Model):
    TASK_TYPES = [
        ('P', 'Personal'),
        ('W', 'Work'),
        ('S', 'Study'),
    ]
    
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=1, choices=TASK_TYPES, default='P')
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='P')
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    
    def __str__(self):
        return self.name