# Generated by Django 5.1.1 on 2024-10-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_loaisanpham_trangthai_alter_sanpham_hinhanh_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='HinhAnh',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
