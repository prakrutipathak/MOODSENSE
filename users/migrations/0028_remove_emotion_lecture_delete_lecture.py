# Generated by Django 4.2.3 on 2023-08-25 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_lecture_emotion_lecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emotion',
            name='lecture',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
