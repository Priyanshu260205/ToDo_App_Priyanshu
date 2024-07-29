from django.db import models


class Mytodo(models.Model):
    task = models.TextField()
    due_at = models.DateField()
    
    is_completed = models.BooleanField(default=False)