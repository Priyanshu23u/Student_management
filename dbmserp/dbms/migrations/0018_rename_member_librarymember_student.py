# Generated by Django 5.1.2 on 2024-11-08 21:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dbms", "0017_remove_registeredstudent_course_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="librarymember",
            old_name="member",
            new_name="student",
        ),
    ]
