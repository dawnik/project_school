# Generated by Django 2.2.7 on 2020-01-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='describe',
            field=models.CharField(default='', max_length=500),
        ),
    ]
