from django.db import models

class BenchmarkModel(models.Model):
    MODEL_STATUS = (
            ('PENDING','PENDING'),
            ('APPROVED', 'APPROVED'),
            ('REJECTED', 'REJECTED'),
            )
    model_mlcube = models.ForeignKey("mlcube.MlCube", on_delete=models.PROTECT)
    benchmark = models.ForeignKey("benchmark.Benchmark", on_delete=models.CASCADE)
    approval_status = models.CharField(choices=MODEL_STATUS,max_length=100, default='PENDING')
    approved_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("model_mlcube", "benchmark"),)
        ordering = ['modified_at']