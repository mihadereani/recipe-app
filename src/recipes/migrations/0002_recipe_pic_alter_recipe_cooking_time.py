# Generated by Django 4.2.1 on 2023-05-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_image.svg', upload_to='recipes'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.FloatField(help_text='In minutes'),
        ),
    ]
