# Generated by Django 4.2.5 on 2023-10-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_contactformsubmission_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformsubmission',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='newslettersubscription',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]