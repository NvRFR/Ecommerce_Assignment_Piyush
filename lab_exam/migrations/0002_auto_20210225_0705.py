# Generated by Django 3.1.7 on 2021-02-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labexam',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
