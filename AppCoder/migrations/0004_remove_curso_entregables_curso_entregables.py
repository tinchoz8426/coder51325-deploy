# Generated by Django 4.0.5 on 2023-04-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_curso_entregables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='entregables',
        ),
        migrations.AddField(
            model_name='curso',
            name='entregables',
            field=models.ManyToManyField(null=True, to='AppCoder.entregable'),
        ),
    ]