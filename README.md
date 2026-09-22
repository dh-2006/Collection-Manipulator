# 🎓 Collection Manipulator

A simple **Python console-based Student Data Organizer** for adding, viewing, updating, and deleting student records.

This project is created to demonstrate basic Python **collections and data handling** in a simple and practical way.

---

## 📌 Project Overview

The **collection manipulator** is a menu-driven Python program that manages student information using:

- List
- Dictionary
- Tuple
- Set
- String Formatting
- Type Casting
- Mutability and Immutability
- Loops and Conditional Statements
- `del` keyword

The program is designed with a simple console interface so that each operation can be performed easily.

---

## ✨ Main Features

| Option | Function |
|---|---|
| ➕ 1 | Add Student |
| 👀 2 | Display All Students |
| ✏️ 3 | Update Student Information |
| 🗑️ 4 | Delete Student |
| 📚 5 | Display Subjects Offered |
| 🚪 6 | Exit |

---

## 🧠 Python Concepts Demonstrated

### 📋 List

Used to store multiple student records.

```python
students = []
```

### 📖 Dictionary

Used to store the information of one student.

```python
student = {
    "student_info": student_info,
    "name": name,
    "age": age,
    "grade": grade,
    "subjects": subjects
}
```

### 🔒 Tuple

Used to store Student ID and Date of Birth together.

```python
student_info = (student_id, student_dob)
```

### 📚 Set

Used to store unique subjects and avoid duplicate subjects.

```python
subjects = set()
```

### 🔤 String Formatting

Used to display student information neatly using f-strings.

### 🔢 Type Casting

Used to convert input values such as Student ID and Age into integers.

### 🔄 Mutability

Student age and subjects can be updated.

### 🔐 Immutability

Student ID and Date of Birth are stored together in a Tuple.

### 🗑️ `del`

Used to delete a student record from the list.

---

## 🖥️ Program Preview

```text
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

---

## 🖼️ Output Preview

See the actual program output:

[![View Output](https://img.shields.io/badge/👀_View_Output-red?style=for-the-badge)](https://github.com/dh-2006/Collection-Manipulator/blob/main/output.png)

---

## 🎥 Project Demo

Watch the complete working demonstration:

[![Watch Demo](https://img.shields.io/badge/▶️_Watch_Project_Demo-blue?style=for-the-badge)](https://drive.google.com/file/d/1SUBl6v0kBstPAPgXk3xNgwcDw2ShthAj/view?usp=sharing)

---

## 💻 Source Code

View the complete Python source code:

[![Open Source Code](https://img.shields.io/badge/💻_View_Source_Code-green?style=for-the-badge)](https://github.com/dh-2006/Collection-Manipulator/blob/main/collection_manipulator.py)
---

## ▶️ How to Run

### Requirements

- Python 3.x
- Any Python IDE or Terminal

### Run the program

```bash
python student_data_organizer.py
```

---

## 📂 Project Structure

```text
Student-Data-Organizer/
│
├── collection_manipulator.py
├── output.png
└── README.md
```

---

## 🎯 Learning Objectives

This project helps in understanding:

- How Python Lists store multiple records
- How Dictionaries organize student information
- How Tuples store fixed information
- How Sets handle unique values
- How user input is handled
- How loops and conditions work
- How mutable data can be updated
- How records can be deleted
- How formatted output can be created

---

## 🔗 How the Concepts Work Together

```text
List
   ↓
Store multiple student records

   ↓

Dictionary
   ↓
Organize one student's information

   ↓

Tuple ─────────→ Student ID + Date of Birth
   ↓

Set ───────────→ Unique Subjects
   ↓

Loops + Conditions
   ↓
Menu-driven Student Data Organizer
```

---

## ✅ Basic Validation

The program performs simple checks for:

- Duplicate Student ID
- Empty Student Name
- Age greater than 0
- Invalid menu choice
- Student not found during update or delete

---

## 🚀 Future Improvements

The project can be extended in the future with:

- 🔍 Search student by ID or name
- 💾 Save records to a file
- 📂 Load saved records
- 📊 Grade or marks management
- 📈 Student performance summary

---

## 👨‍💻 Project Information

**Project:** collection_manipulator  
**Language:** Python  
**Type:** Console-Based Application  
**Purpose:** Python Collection Manipulation Project

---

⭐ **Thank you for checking out the project!**
