# Generated by Django 5.1.1 on 2024-09-04 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0002_bass_brand_bass_color_bass_description_bass_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(max_length=50),
        ),
    ]
