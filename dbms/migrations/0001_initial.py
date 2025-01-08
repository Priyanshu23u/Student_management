# Generated by Django 4.2.13 on 2024-10-21 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CertificateApplication",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=10,
                    ),
                ),
                ("application_date", models.DateField()),
                ("issued_date", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="CertificateType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("certificate_name", models.CharField(max_length=255)),
                ("fee", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("submitted_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Enquiry",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("student_name", models.CharField(max_length=255)),
                ("enquiry_text", models.TextField()),
                ("submitted_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="ImageGallery",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image_url", models.CharField(max_length=255)),
                ("caption", models.CharField(max_length=255)),
                ("uploaded_by", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="LibraryInventory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("book_name", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("category", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="NewsNotice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("date_posted", models.DateField()),
                ("posted_by", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Slider",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image_url", models.CharField(max_length=255)),
                ("caption", models.CharField(max_length=255)),
                ("order", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="StreamCourse",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("stream_name", models.CharField(max_length=255)),
                ("course_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Ticker",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("message", models.CharField(max_length=255)),
                ("date_created", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="VideoGallery",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("video_url", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("uploaded_by", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="RegisteredStudent",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("student_name", models.CharField(max_length=255)),
                ("admission_date", models.DateField()),
                (
                    "fee_status",
                    models.CharField(
                        choices=[("Paid", "Paid"), ("Unpaid", "Unpaid")], max_length=10
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.streamcourse",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LibraryMember",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("membership_date", models.DateField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.registeredstudent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LibraryFineCollection",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_paid", models.DateField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.registeredstudent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Grievance",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("grievance_type", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Resolved", "Resolved"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=10,
                    ),
                ),
                ("submitted_date", models.DateField()),
                ("resolved_date", models.DateField(blank=True, null=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.registeredstudent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("feedback_text", models.TextField()),
                ("submitted_date", models.DateField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.registeredstudent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeeCollection",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_paid", models.DateField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.registeredstudent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("designation", models.CharField(max_length=255)),
                ("contact", models.CharField(max_length=100)),
                ("photo_url", models.CharField(max_length=255)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CertificateFeeCollection",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_paid", models.DateField()),
                (
                    "certificate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.certificateapplication",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CertificateDistribution",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("distributed_date", models.DateField()),
                (
                    "certificate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.certificateapplication",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="certificateapplication",
            name="certificate",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dbms.certificatetype"
            ),
        ),
        migrations.AddField(
            model_name="certificateapplication",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dbms.registeredstudent"
            ),
        ),
        migrations.CreateModel(
            name="BookIssued",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("issue_date", models.DateField()),
                ("return_date", models.DateField()),
                (
                    "fine_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.libraryinventory",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.librarymember",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdmissionStat",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("year", models.IntegerField()),
                ("total_admissions", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbms.streamcourse",
                    ),
                ),
            ],
        ),
    ]
