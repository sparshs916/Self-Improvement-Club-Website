# Generated by Django 4.2.1 on 2023-05-29 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0002_remove_userprofile_profilepic_userprofile_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="profile",
            new_name="profileImage",
        ),
    ]
