# Generated by Django 3.2 on 2021-11-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20211121_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicos',
            name='card',
        ),
        migrations.AddField(
            model_name='servicos',
            name='card',
            field=models.ManyToManyField(blank=True, null=True, to='landing.Card'),
        ),
    ]
