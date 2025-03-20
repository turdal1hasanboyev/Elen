from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models in the application.
    """
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Model'
