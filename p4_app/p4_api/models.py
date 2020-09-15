from django.db import models
from p4_app.authentication.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='games', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image_url = models.URLField
    description = models.TextField(blank=True)
    additional_info = models.CharField(max_length=5000)
    added = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title