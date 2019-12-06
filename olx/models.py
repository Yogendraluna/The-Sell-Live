import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="static/images/")
    phone_number = PhoneNumberField(null=False, blank=False, help_text="Contact Number")

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    
