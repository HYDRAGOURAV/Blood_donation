# Generated by Django 5.0.3 on 2024-03-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0006_delete_data_req_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delete_data_req',
            name='Delete_Contact_req',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='delete_data_req',
            name='Delete_city_req',
            field=models.CharField(max_length=20),
        ),
    ]
