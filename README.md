# College Management System

This Django-based project is a comprehensive system designed for managing various entities and workflows within a college. It integrates academic, financial, library, and administrative functions to streamline operations for students, faculty, and administrators.

## Overview

The College Management System (CMS) manages users (students, faculty, and admins), courses, departments, news, media galleries, certificates, grievances, feedback, financial records, and library resources. Each feature is represented by a model that defines relationships between entities and provides essential validations and constraints to maintain data integrity.

## ER Diagram

The Entity-Relationship (ER) diagram for this project illustrates the relationships between key entities in the system. 

**Key Entities and Relationships:**

1. **User Management**
   - `User` (Django's built-in model) is extended through the `Profile` model to categorize users as admins, faculty, or students.
   - Each `Profile` can be linked to a unique `faculty_id` or `student_id`.

2. **Department and Course Management**
   - Departments are managed by the `Department` model, while `StreamCourse` organizes streams and courses.
   - Faculty members are assigned to departments and courses through `FacultyCourseAssignment`.

3. **Academic Records**
   - `RegisteredStudent` holds student enrollment details, while `CourseMarks` records their academic performance with course-specific marks.

4. **Financial Management**
   - `FeeCollection` and `LibraryFineCollection` track students' financial transactions, including fee payments and library fines.

5. **Library Management**
   - `LibraryInventory` manages book stocks, `LibraryMember` handles memberships, and `BookIssued` records issued books with validations to maintain stock.

6. **Certificate Management**
   - `CertificateType` defines available certificates, and `CertificateApplication` processes student applications.

7. **Grievances and Feedback**
   - Students can submit `Grievance` records for issue reporting and `Feedback` for course and faculty evaluations.

### ER Diagram

![Untitled](https://github.com/user-attachments/assets/0dcbbe6f-132f-4d57-86f6-5b91a156f9cf)


This simplified ER diagram illustrates core relationships:
- **One-to-Many**: `Department` to `Faculty`, `StreamCourse` to `FacultyCourseAssignment`.
- **Many-to-Many**: `RegisteredStudent` to `StreamCourse` through enrollment, `Faculty` to `StreamCourse` through course assignments.

---

## Features

1. **User Management**: Custom user roles (admin, faculty, student) with personalized views and permissions.
2. **Department and Faculty Management**: Department creation and faculty assignments.
3. **Course Enrollment and Student Records**: Handles student registrations and enrollments with details on admission dates and fee statuses.
4. **Academic Tracking**: Course marks are validated by faculty assignments to ensure data accuracy.
5. **Financial Records**: Tracks student fee payments and fines for efficient financial management.
6. **Library System**: Comprehensive inventory and issue-return tracking with fine management.
7. **Certificate Applications**: Facilitates certificate requests and manages approval and issuance dates.
8. **Grievance and Feedback Handling**: Collects and manages student feedback and grievances to ensure issue tracking and resolution.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Astha-Pathak/Student_management.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dbmserp
   ```
4. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## Usage

- **Admin Dashboard**: For managing departments, users, and academic records.
- **Faculty Portal**: Manages courses, grading, and student feedback.
- **Student Portal**: Provides access to enrollment, academic records, and certificate applications.

## Contribution

Contributions to enhance the system are welcome. Please submit a pull request or open an issue for any suggestions or bug reports.

## License

This project is open-source and available under the [MIT License](LICENSE).
