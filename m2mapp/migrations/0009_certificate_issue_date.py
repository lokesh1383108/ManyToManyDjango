# Generated by Django 4.2.6 on 2023-10-19 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('m2mapp', '0008_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='issue_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
