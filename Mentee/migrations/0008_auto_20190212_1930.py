# Generated by Django 2.1.5 on 2019-02-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mentee', '0007_auto_20190212_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='foto_mentee',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]