# Generated by Django 5.1.2 on 2024-11-04 21:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dbms", "0013_rename_student_librarymember_member"),
    ]

    operations = [
        migrations.RenameField(
            model_name="librarymember",
            old_name="member",
            new_name="student",
        ),
    ]
