# Generated by Django 3.2.4 on 2021-07-11 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('ubication', models.CharField(max_length=100)),
                ('wifi', models.BooleanField()),
                ('garage', models.BooleanField()),
                ('pool', models.BooleanField()),
                ('bathrooms', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1)),
                ('rooms', models.CharField(choices=[('1', 'Individual'), ('2', 'Parejas'), ('3', '2 Adultos un niño'), ('4', '4 Personas '), ('5', '5 Personas '), ('6', 'Hasta 8 personas ')], max_length=1)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
