# Generated by Django 3.2.3 on 2021-05-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0005_consumer_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='completed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
