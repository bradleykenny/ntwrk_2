# Generated by Django 2.0.7 on 2018-07-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180729_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.ImageField(default='dp/placeholder2.png', upload_to='dp/'),
        ),
    ]
