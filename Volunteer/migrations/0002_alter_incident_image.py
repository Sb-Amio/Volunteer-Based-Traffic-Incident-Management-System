# Generated by Django 5.0.2 on 2024-10-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]