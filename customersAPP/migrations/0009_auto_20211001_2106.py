# Generated by Django 3.1.2 on 2021-10-02 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customersAPP', '0008_auto_20211001_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='lastupdateuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customersAPP.user'),
        ),
    ]
