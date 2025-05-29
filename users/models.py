from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,
                            unique=True)
    slug = models.SlugField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:saunas_list_by_category',
                        args=[self.slug])

class Saunas(models.Model):
    category = models.ForeignKey(Category,
                                 related_name="products",
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='saunas/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=10,
                                         decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(default=0.00,
                                   max_digits=4,
                                   decimal_places=2)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id","slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]
        verbose_name = "Сауна"
        verbose_name_plural = "Сауны"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:sauna_detail',
                        args=[self.slug])

    def sell_price(self):
        if self.discount:
            return round(self.price_per_hour - self.price_per_hour * self.discount / 100,2)

