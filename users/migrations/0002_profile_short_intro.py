# Generated by Django 4.0.10 on 2024-02-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='short_intro',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]