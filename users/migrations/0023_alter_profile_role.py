# Generated by Django 4.2.3 on 2023-07-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('User', 'User')], default='Select your role', max_length=50, null=True),
        ),
    ]
