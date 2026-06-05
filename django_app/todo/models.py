from django.db import models
from django.utils import timezone

class Todo(models.Model):
    # Betulkan koma yang hilang dan ejaan PRIORITY
    PRIORITY_CHOICES = [
        ('L', 'Low'),       # <-- Letak koma di sini
        ('M', 'Medium'),    # <-- Letak koma di sini
        ('H', 'High'),      # <-- Elok letak koma juga di sini (best practice Python)
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    
    # Pastikan nama di bahagian choices=... ini juga dikemaskini mengikut nama di atas
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        if self.due_date and not self.is_completed:
            return timezone.now() > self.due_date
        return False
