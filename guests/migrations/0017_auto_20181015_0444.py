# Generated by Django 2.1.2 on 2018-10-15 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_party_rehearsal_dinner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guests.Party'),
        ),
    ]
