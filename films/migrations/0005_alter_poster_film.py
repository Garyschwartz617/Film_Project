# Generated by Django 3.2.6 on 2021-08-24 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_alter_commentary_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='film',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='films.film'),
        ),
    ]
