# Generated by Django 5.0.1 on 2024-01-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_mailing_name_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(default='создана', max_length=50, verbose_name='статус'),
        ),
    ]
