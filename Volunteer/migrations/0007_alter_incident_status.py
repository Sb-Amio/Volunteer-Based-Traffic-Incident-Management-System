# Generated by Django 5.0.2 on 2024-10-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0006_alter_incident_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='status',
            field=models.CharField(choices=[('no action', 'No Action'), ('on action', 'On Action'), ('completed', 'Completed')], default='No Action', max_length=20),
        ),
    ]