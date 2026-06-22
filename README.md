<img width="1456" height="720" alt="Institution Information Management System" src="https://github.com/user-attachments/assets/5973ae00-59f2-48bc-8ffc-f663877fcc58" />

# 🏫 Institution Information Management System

An **Institution Information Management System** developed using **Python Django** to streamline the management of academic information within an educational institution. The application provides a centralized platform for managing courses and student records through an intuitive web interface.

Built on Django's **Model-View-Template (MVT)** architecture, the system demonstrates essential CRUD (Create, Read, Update, Delete) operations while maintaining a clean and organized user experience.

---

## ✨ Features

### 📚 Course Management

* Add new courses
* View available courses
* Display detailed course information
* Edit and update course records
* Manage academic offerings

### 👨‍🎓 Student Management

* Student registration
* View student details
* Edit student information
* Maintain student records

### 🌐 General Features

* Responsive web interface
* Home page with institution overview
* Template-based frontend
* User-friendly navigation
* Dynamic data management

---

## 🏗️ Technology Stack

| Component    | Technology                |
| ------------ | ------------------------- |
| Backend      | Python 3                  |
| Framework    | Django                    |
| Frontend     | HTML5, CSS3               |
| Database     | SQLite (Default)          |
| Architecture | Model-View-Template (MVT) |

---

## 📂 Project Structure

```text
institution-management/
│
├── institution/            # Project configuration
├── app/                    # Main application
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 📄 Pages Included

| Page                  | Description                                        |
| --------------------- | -------------------------------------------------- |
| **home.html**         | Landing page of the application                    |
| **course.html**       | Displays all available courses                     |
| **cour_det.html**     | Shows detailed information about a selected course |
| **registration.html** | Student registration form                          |
| **student.html**      | Displays registered students                       |
| **edit_cou.html**     | Update existing course information                 |
| **edit_stud.html**    | Update student records                             |
| **details.html**      | View complete student details                      |

---

## 🧩 Core Modules

* Home Module
* Course Management
* Student Registration
* Student Management
* Course Details
* Student Details
* Record Update Module

---

## 🔄 Application Workflow

```text
Home
 │
 ▼
View Courses
 │
 ├── Course Details
 │
 ▼
Student Registration
 │
 ▼
Student Records
 │
 ├── View Details
 ├── Edit Student
 └── Edit Course
```

---

## 🔒 Key Functionalities

* Course Creation and Management
* Student Registration
* Record Viewing
* Record Updating
* Dynamic Data Rendering
* Django Template Rendering
* Database Integration

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* Django
* Virtual Environment (Recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/institution-management.git

# Navigate to the project directory
cd institution-management

# Create a virtual environment
python -m venv venv

# Activate the virtual environment

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Visit the application at:

```text
http://127.0.0.1:8000/
```

---

## 📈 Future Enhancements

* Faculty Management
* Attendance Management
* Student Authentication
* Department Management
* Examination Module
* Result Management
* File Uploads
* Search and Filtering
* Dashboard Analytics
* Role-Based Access Control

---

## 📄 License

This project is intended for educational and portfolio purposes. Feel free to modify and extend it according to your learning requirements.

---

## 👨‍💻 Author

**Pauljo George**

If you found this project useful, consider giving it a ⭐ on GitHub.
