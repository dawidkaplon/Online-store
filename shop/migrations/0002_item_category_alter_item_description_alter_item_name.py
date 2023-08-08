# Generated by Django 4.2.3 on 2023-08-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]