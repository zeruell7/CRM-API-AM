# Generated by Django 3.1.2 on 2021-10-02 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customersAPP', '0006_auto_20211001_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='lastupdateuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customersAPP.user'),
        ),
    ]
