Hospital Management System
This is a simple command-line-based Hospital Management System developed in Python. It allows for the management of doctors, patients, and hospital staff, with options to add, update, display, and delete records. The system also supports creating appointments and generating bills, making it a comprehensive tool for small clinics or hospitals.

Features
Doctor Management: Add, display, update, and delete doctor records.
Patient Management: Add, display, update, and delete patient records.
Hospital Staff Management: (Placeholder, can be extended as needed.)
Appointment Management: Schedule appointments between patients and doctors.
Billing: Generate and view patient bills.


Classes and Structure
Person (abstract): Parent class for common attributes such as name, age, and address.
Doctor, Patient, HospitalStaff: Child classes with unique properties:
Doctor: Includes specialization and years_of_experience.
Patient: Includes medical_history.
Hospital: Manages records for doctors and patients.
Appointment: Creates and displays appointment details.