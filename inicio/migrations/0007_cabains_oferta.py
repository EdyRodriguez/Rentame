# Generated by Django 3.2.6 on 2021-08-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_alter_cabains_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabains',
            name='oferta',
            field=models.BooleanField(default=False),
        ),
    ]