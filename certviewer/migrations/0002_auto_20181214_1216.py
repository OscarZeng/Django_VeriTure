# Generated by Django 2.0.4 on 2018-12-14 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certviewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='logoImg',
            field=models.ImageField(upload_to=''),
        ),
    ]
