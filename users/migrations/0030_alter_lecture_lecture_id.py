# Generated by Django 4.2.3 on 2023-08-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
