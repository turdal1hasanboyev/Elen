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


class SubEmail(BaseModel):
    """
    Model for sub email.
    """

    sub_email = models.EmailField(max_length=100, null=True, blank=True, unique=True, db_index=True)

    class Meta:
        """
        Meta class for SubEmail model.
        """

        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emails'

    def __str__(self):
        """
        String representation of the model.
        """

        return f"{self.sub_email}"
