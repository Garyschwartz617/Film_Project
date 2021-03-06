# Generated by Django 3.2.6 on 2021-08-23 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('explanation_img', models.CharField(max_length=80)),
                ('film', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='films.film')),
            ],
        ),
    ]
