# Generated by Django 3.1.5 on 2021-03-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='todo',
            name='pdf',
            field=models.FileField(default='', upload_to='pdfs/'),
        ),
    ]
