# Generated by Django 3.2.3 on 2021-05-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0006_alter_request_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
