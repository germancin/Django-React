# Generated by Django 2.0.5 on 2018-05-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]