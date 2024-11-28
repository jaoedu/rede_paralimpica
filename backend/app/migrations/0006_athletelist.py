# Generated by Django 5.1.2 on 2024-11-27 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_athlete_modalities_remove_sponsor_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('functional_classification', models.CharField(max_length=100)),
                ('modalities', models.ManyToManyField(blank=True, to='app.modality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
