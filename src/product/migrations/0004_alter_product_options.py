# Generated by Django 3.2.8 on 2022-11-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productvariant_variant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
    ]
