# Generated by Django 3.2 on 2021-11-25 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20211121_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('texto1', models.CharField(max_length=5000)),
                ('textoDestaque', models.CharField(max_length=5000)),
                ('textoConclusao', models.CharField(max_length=5000)),
                ('imagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.imagem')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='landing.Tag')),
            ],
        ),
    ]
