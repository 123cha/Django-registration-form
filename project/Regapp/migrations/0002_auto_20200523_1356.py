# Generated by Django 3.0.6 on 2020-05-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='No',
            new_name='Sem',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key='True', serialize=False),
        ),
    ]
