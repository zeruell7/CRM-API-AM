# Generated by Django 3.1.2 on 2021-10-02 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customersAPP', '0007_auto_20211001_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumer',
            name='createuser',
        ),
        migrations.AddField(
            model_name='costumer',
            name='creatoruser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='creatoruser', to='customersAPP.user'),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='lastupdateuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customersAPP.user'),
        ),
    ]
