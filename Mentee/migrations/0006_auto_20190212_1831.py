# Generated by Django 2.1.5 on 2019-02-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mentee', '0005_auto_20190212_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='foto_mentee',
            field=models.CharField(max_length=300),
        ),
    ]
