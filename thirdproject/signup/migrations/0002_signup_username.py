# Generated by Django 3.0.2 on 2020-05-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
