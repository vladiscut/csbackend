# Generated by Django 4.1.7 on 2023-03-15 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_alter_review_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="product",
                to="product.producttype",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="regular_price",
            field=models.PositiveBigIntegerField(
                blank=True, verbose_name="Старая цена"
            ),
        ),
    ]
