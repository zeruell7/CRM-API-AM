# Generated by Django 3.1.2 on 2021-10-02 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customersAPP', '0011_auto_20211001_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costumer',
            old_name='creatoruser',
            new_name='creatoruser_id',
        ),
    ]
