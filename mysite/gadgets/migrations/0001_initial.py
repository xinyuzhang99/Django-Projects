# Generated by Django 4.0.7 on 2023-02-24 18:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Brand must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('price', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('notes', models.CharField(max_length=300)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gadgets.brand')),
            ],
        ),
    ]
