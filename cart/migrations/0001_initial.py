# Generated by Django 3.2.12 on 2022-04-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(default=0)),
                ('currency', models.CharField(max_length=5)),
                ('items_number', models.IntegerField(default=0)),
                ('total_discounted', models.FloatField(default=0)),
                ('amount_discounted', models.FloatField(default=0)),
                ('payment_status', models.CharField(default='pending', max_length=35)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
