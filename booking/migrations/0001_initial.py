# Generated by Django 3.2.20 on 2023-07-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people', models.PositiveIntegerField()),
                ('message', models.TextField(blank=True)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]
