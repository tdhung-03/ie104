# Generated by Django 4.2.1 on 2023-05-31 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_product_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="products/images"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="image_public_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]