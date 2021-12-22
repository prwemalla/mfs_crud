from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class task(models.Model):
    
    # Status Choices
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING'
        DONE = 'DONE'
    
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(max_length=100)
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("task_service_task_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("task_service_task_update", args=(self.pk,))
