# Generated by Django 5.1.4 on 2025-01-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='프로필 사진'),
        ),
    ]
