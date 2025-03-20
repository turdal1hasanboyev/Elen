from django.db import models

from django.utils.text import slugify

from apps.common.models import BaseModel


class Tag(BaseModel):
    """
    Tag model.
    """

    name = models.CharField(max_length=225, db_index=True, unique=True)
    slug = models.SlugField(max_length=225, unique=True,
                            blank=True, null=True, db_index=True)

    class Meta:
        """
        Meta class for Tag model.
        """

        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def save(self, *args, **kwargs):
        """
        Save method for Tag model.
        """

        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of Tag model.
        """

        return f"{self.name}"


class Category(BaseModel):
    """
    Category model.
    """

    name = models.CharField(max_length=225, db_index=True, unique=True)
    slug = models.SlugField(max_length=225, unique=True,
                            blank=True, null=True, db_index=True)

    class Meta:
        """
        Meta class for Category model.
        """

        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        """
        Save method for Category model.
        """

        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of Category model.
        """

        return f"{self.name}"
