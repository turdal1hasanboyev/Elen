from django.db import models

from django.urls import reverse
from django.utils.text import slugify

from apps.common.models import BaseModel
from apps.category.models import Tag, Category


class Blog(BaseModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='blog_tag')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    author = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE, related_name='blog_author')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        """
        Meta class for Blog model.
        """

        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        """
        Return a string representation of the model.
        """

        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        """
        Save the model instance.
        """

        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self, *args, **kwargs):
        """
        Return the absolute URL of the model.
        """

        return reverse('blog-detail', kwargs={'slug': self.slug})
    