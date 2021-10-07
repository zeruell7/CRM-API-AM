# Generated by Django 3.1.2 on 2021-10-02 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customersAPP', '0010_auto_20211001_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='creatoruser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='creatoruser', to='customersAPP.user'),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='lastupdateuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lastupdateuser', to='customersAPP.user'),
        ),
    ]