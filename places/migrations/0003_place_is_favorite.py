# Generated by Django 2.0.5 on 2018-06-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20180608_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
