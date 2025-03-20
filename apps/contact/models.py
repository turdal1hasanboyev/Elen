from django.db import models

from apps.common.models import BaseModel


class Contact(BaseModel):
    """
    Contact model
    """
    
    name = models.CharField(max_length=150, db_index=True)
    email = models.EmailField(max_length=150, db_index=True, unique=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        """
        Meta class for Contact model.
        """

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """
        Return a string representation of the model.
        """

        return f"{self.name}"
    