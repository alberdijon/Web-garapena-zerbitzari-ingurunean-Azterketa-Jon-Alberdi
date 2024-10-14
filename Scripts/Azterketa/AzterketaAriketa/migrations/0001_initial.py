# Generated by Django 5.1.1 on 2024-10-14 06:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medikua',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('izena', models.CharField(max_length=75)),
                ('abizena', models.CharField(max_length=100)),
                ('lanpostua', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pazientea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('izena', models.CharField(max_length=75)),
                ('abizena', models.CharField(max_length=100)),
                ('historiala', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='zita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('mediku_kodea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AzterketaAriketa.medikua')),
                ('paziente_kodea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AzterketaAriketa.pazientea')),
            ],
        ),
    ]
