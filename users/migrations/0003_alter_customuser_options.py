# Generated by Django 5.1.1 on 2024-10-15 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
