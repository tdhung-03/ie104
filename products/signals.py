import cloudinary
import cloudinary.uploader
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product


@receiver(post_save, sender=Product)
def upload_image_to_cloudinary(sender, instance, created, **kwargs):
    if created and instance.image:
        upload_result = cloudinary.uploader.upload(instance.image.path)
        instance.image_public_id = upload_result['public_id']
        instance.save()
