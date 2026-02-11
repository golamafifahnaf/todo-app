# 📝 TodoApp (CLI)

A clean and structured Command Line Interface (CLI) based Todo Application built with Python.

This project demonstrates real-world concepts such as command parsing, data persistence, lifecycle management, and clean separation between UI and logic.

---

## 🚀 Current Version: v1.0 (Stable)

This is the first stable release of TodoApp.

### ✨ Features

- Add new tasks
- Update existing tasks
- Delete specific tasks
- Mark tasks as completed
- Mark all tasks as completed (`DONE ALL`)
- Delete completed tasks (`DLT DONE`)
- Delete all tasks (`DLT ALL`)
- Persistent storage using JSON
- Clean and structured command parsing
- Defensive input validation
- Colorized CLI output for better UX

---

## 🧪 Previous Version

`v1.0-beta`

The beta version included core CLI functionality but did not support persistent storage or advanced lifecycle features.

---

## 🧠 Concepts Practiced

- File handling (JSON)
- Error handling
- Data structures (List of Dictionaries)
- Separation of concerns
- Command routing
- CLI UX design
- Version tagging & release workflow

---

## 📁 Project Structure

todo_app/
│
├── cli/
│ ├── todo_app_cli.py
│ └── storage.py
│
├── README.md
└── .gitignore

---

## 💾 Storage System

Tasks are stored in a `tasks.json` file located in the project root directory.

The file is automatically created if it does not exist.

---

## ▶️ How to Run

Navigate to the project root:
cd todo_app
python cli/todo_app_cli.py

---

## 📌 Future Plans

- Refactor into class-based architecture
- Convert CLI version into a web-based version
- Add database integration
- Improve command router system
- Introduce automated tests
