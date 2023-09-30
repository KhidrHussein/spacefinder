# Generated by Django 4.2.5 on 2023-09-30 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='space',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='space',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='space',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='space',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
