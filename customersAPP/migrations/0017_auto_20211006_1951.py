# Generated by Django 3.1.2 on 2021-10-07 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customersAPP', '0016_auto_20211006_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='creatoruser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='creatoruser', to=settings.AUTH_USER_MODEL),
        ),
    ]
