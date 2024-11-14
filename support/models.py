from django.db import models
from customers.models import ServiceRequest
from django.contrib.auth.models import User

class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_requests = models.ManyToManyField(ServiceRequest, blank=True)

    def __str__(self):
        return self.user.username
