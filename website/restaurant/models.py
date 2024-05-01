from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='restaurant/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate slug based on the name
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"