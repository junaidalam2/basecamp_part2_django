# Generated by Django 5.1.1 on 2024-10-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboards', '0002_message_last_updated_by_thread_last_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='topic',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='thread',
            name='message_text',
            field=models.TextField(blank=True),
        ),
    ]
