# Generated by Django 2.2.10 on 2020-05-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200504_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(blank=True, default='07559E', max_length=6, verbose_name='Code'),
        ),
    ]