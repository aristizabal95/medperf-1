from django.db import models

class BenchmarkDataset(models.Model):
    DATASET_STATUS = (
            ('PENDING','PENDING'),
            ('APPROVED', 'APPROVED'),
            ('REJECTED', 'REJECTED'),
            )
    dataset = models.ForeignKey("dataset.Dataset", on_delete=models.PROTECT)
    benchmark = models.ForeignKey("benchmark.Benchmark", on_delete=models.CASCADE)
    approval_status = models.CharField(choices=DATASET_STATUS,max_length=100)
    approved_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("dataset", "benchmark"),)
        ordering = ['modified_at']