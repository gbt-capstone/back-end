# Generated by Django 4.2.1 on 2023-05-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('address', models.CharField(max_length=150, verbose_name='주소')),
            ],
        ),
    ]