# Generated by Django 4.2.6 on 2023-10-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m2mapp', '0002_alter_teacher_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]