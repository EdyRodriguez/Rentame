# Generated by Django 3.2.6 on 2021-08-23 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_alter_cabains_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cabains',
            options={'ordering': ['-created'], 'verbose_name': 'Cabaña', 'verbose_name_plural': 'Cabañas'},
        ),
    ]
