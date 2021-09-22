from django.db import models
from django.contrib.auth.models import User

class BenchmarkUser(models.Model):
    #USER_STATUS = (
    #        ('APPROVED', 'APPROVED'),
    #        ('REJECTED', 'REJECTED'),
    #        ('PENDING','PENDING'),
    #        )
    
    USER_ROLES = (
            ('BenchmarkOwner','BenchmarkOwner'),
            ('DataOwner', 'DataOwner'),
            ('ModelOwner', 'ModelOwner'),
            )

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    benchmark = models.ForeignKey("benchmark.Benchmark", on_delete=models.CASCADE)
    role = models.CharField(choices=USER_ROLES,max_length=100)
    #approval_status = models.CharField(choices=USER_STATUS,max_length=100, default='APPROVED')
    #approved_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("user", "benchmark", "role"),)
        ordering = ['modified_at']
