# Generated by Django 4.0.5 on 2022-07-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobregnome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
        ),
    ]
