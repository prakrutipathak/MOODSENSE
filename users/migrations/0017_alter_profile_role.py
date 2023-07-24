# Generated by Django 4.2.3 on 2023-07-24 14:08

from django.db import migrations, models
from django.contrib.auth.models import Group


def create_groups(apps, schema_editor):
    Group.objects.get_or_create(name='Faculty')
    Group.objects.get_or_create(name='Admin')
    Group.objects.get_or_create(name='FeedbackbackOfficer')



class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20230723_2238'),
    ]




    operations = [
        migrations.RunPython(create_groups),
    ]