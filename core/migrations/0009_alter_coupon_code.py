# Generated by Django 5.1.2 on 2024-10-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_billingaddress_id_alter_category_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
