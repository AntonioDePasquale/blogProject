# Generated by Django 4.2.16 on 2024-09-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentAuthor',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentContent',
            field=models.TextField(),
        ),
    ]
