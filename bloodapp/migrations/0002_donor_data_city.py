# Generated by Django 5.0 on 2024-02-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor_data',
            name='City',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]