# Generated by Django 5.1.3 on 2024-12-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('thing', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
            ],
        ),
    ]