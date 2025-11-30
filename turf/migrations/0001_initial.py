import json
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.TextField()),  # Changed to TextField to store JSON string
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('week', models.TextField()),  # Changed to TextField to store JSON string
            ],
        ),
        migrations.CreateModel(
            name='TurfBooked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('selected_date', models.CharField(max_length=200)),
                ('current_date', models.CharField(max_length=200)),
                ('booking_time', models.CharField(default='', max_length=200)),
                ('slots', models.TextField()),  # Changed to TextField to store JSON string
                ('payment_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='turfBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(max_length=12)),
                ('isBooked', models.BooleanField(default=False)),
                ('days', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
