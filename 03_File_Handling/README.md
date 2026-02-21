# 📂 Python File Handling 

Welcome to my **Python File Handling** repository! This project is a comprehensive collection of scripts designed to master the `os`, `json`, `csv` modules in Python.

---

## ⚠️ Important: Multi-Logic Files
To provide a complete learning experience, some files (like `problem_02.py`) contain **multiple approaches** to the same problem. 

**If you wish to test a specific method:**
1.  **Read the Comments:** I have labeled "First Approach," "Second Approach," or "Method" within the code.
2.  **Comment/Uncomment:** Ensure only one logic block is active (uncommented) at a time to avoid duplicate outputs or file conflicts.

---

## 🛠️ Repository Roadmap

### 📘 Core Concepts
| File Name | Key Concepts | Description |
| :--- | :--- | :--- |
| **01_write_read_file.py** | `w`, `r`, `a`, `readline()` | Basic file I/O operations and different ways to read data. |
| **02_with_statement.py** | `with` context manager | Handling tuples, lists, and dictionaries safely using context managers. |
| **05_serialization.py** | `json.dump()`, `json.load()` | Handling complex data like nested lists and dictionaries using JSON. |
| **06_OS.py** | `os.path.exists`, `os.rename` | Interacting with the operating system to manage, rename, and delete files. |
| **07_csv.py** | `csv.writer`, `csv.reader` | Structured data handling for student records using the CSV module. |

### 📝 Problem Solving & Logic
| File Name | Problem Type | Description |
| :--- | :--- | :--- |
| **problem_01.py** | Character Iteration | Reads a file exactly one character at a time using `read(1)`. |
| **problem_02.py** | Line Numbering | **Contains 2 Approaches:** Demonstrates `readline()` vs. direct file iteration. |
| **problem_03.py** | Content Transformation | Writes a paragraph and performs string replacement (e.g., "Growth" to "Success"). |
| **problem_04.py** | Word Searching | Iterates through a file to find a specific word and report its exact line number. |
| **problem_05.py** | Data Analysis | Parses a comma-separated string of numbers and calculates totals for even/odd values. |

---

## 📊 Quick Reference: File Modes



* **`r`**: **Read-only**. The default mode; throws an error if the file does not exist.
* **`w`**: **Write-only**.Creates a new file or **overwrites** existing content.
* **`a`**: **Append**.Adds data to the end of the file without deleting existing content.
* **`w+` / `r+`**: **Reading and Writing**. Useful for simultaneous operations like JSON `dump` and `load` cycles.

---

