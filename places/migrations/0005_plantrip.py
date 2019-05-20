# Generated by Django 2.0.5 on 2018-06-22 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20180610_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('priority', models.CharField(max_length=1400000000000000000)),
                ('placename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.City')),
            ],
        ),
    ]
