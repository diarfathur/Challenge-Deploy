# Generated by Django 2.1.5 on 2019-02-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mentee', '0006_auto_20190212_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='foto_mentee',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
