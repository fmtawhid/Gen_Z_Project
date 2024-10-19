# Generated by Django 5.0.6 on 2024-05-19 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_gallerymodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('bookingDate', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel')),
            ],
        ),
    ]