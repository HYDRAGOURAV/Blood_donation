# Generated by Django 5.0 on 2024-02-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0004_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=30)),
                ('User_email', models.EmailField(max_length=30)),
                ('User_message', models.TextField()),
            ],
        ),
    ]
