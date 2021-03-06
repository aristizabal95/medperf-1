from django.db import models
from django.contrib.auth.models import User

class Benchmark(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True)
    docs_url = models.CharField(max_length=100, blank=True)
    owner =  models.ForeignKey(User, on_delete=models.PROTECT)
    data_preparation_mlcube = models.ForeignKey("mlcube.MlCube", on_delete=models.PROTECT, related_name="data_preprocessor_mlcube")
    reference_model_mlcube = models.ForeignKey("mlcube.MlCube", on_delete=models.PROTECT, related_name="reference_model_mlcube")
    data_evaluator_mlcube = models.ForeignKey("mlcube.MlCube", on_delete=models.PROTECT, related_name="data_evaluator_mlcube" )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['modified_at']
