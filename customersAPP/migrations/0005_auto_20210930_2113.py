# Generated by Django 3.1.2 on 2021-10-01 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customersAPP', '0004_auto_20210930_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='lastupdateuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customersAPP.user'),
        ),
    ]