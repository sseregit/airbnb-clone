# Generated by Django 2.2.5 on 2021-09-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedday',
            name='created',
            field=models.DateField(null=True,blank=True),
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='updated',
            field=models.DateField(null=True,blank=True),
        ),
    ]
