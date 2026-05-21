# DevOps Python Learning Repository

## Overview

A learning-focused repository for Python automation, API integration, networking, and PostgreSQL database workflows tailored to DevOps and infrastructure practitioners. It contains sample scripts for Python fundamentals, file operations, HTTP APIs, scheduling, web scraping, socket programming, and database automation.

**Target Audience:** DevOps Engineers, Python Developers, Automation Specialists  
**Skill Level:** Beginner to Intermediate  
**Python Version:** 3.12+

---

## 📋 Updated Project Structure

```
devops-python/
├── 1-hello.py
├── 2-fileread.py
├── 2-filewrite.py
├── 3-fileoperations.py
├── 4-ifelse.py
├── 4-loops.py
├── 4-break-continue.py
├── 4-oddeven.py
├── 5-functions.py
├── 5-modules.py
├── math_operations.py
├── networking/
│   ├── 6-networking-client.py
│   ├── 6-networking-request.py
│   ├── 6-networking-scap.py
│   └── 6-networking-server.py
├── sockets/
│   ├── client.py
│   ├── server.py
│   └── soc.py
├── apis/
│   ├── api-ex.py
│   └── api-req.py
├── automation/
│   ├── getlinks.py
│   ├── par.py
│   ├── par2.py
│   ├── task_schedule.py
│   └── output.json
├── python-postgres/
│   └── postgres-python.py
├── requirements.txt
├── devops-python-venv/
├── arjun.txt
└── README.md
```

---

## 🎯 Learning Modules

### 1. **Python Fundamentals** (Modules 1-4)

| File | Topic | Key Concepts |
|------|-------|--------------|
| `1-hello.py` | Basic Syntax | Variables, data types, print output |
| `2-fileread.py` | File Reading | File opening, reading, closing |
| `2-filewrite.py` | File Writing | Writing text files, file persistence |
| `3-fileoperations.py` | File Utilities | Rename, delete, and filesystem checks |
| `4-ifelse.py` | Conditionals | If/elif/else logic, boolean evaluation |
| `4-loops.py` | Iteration | For loops, while loops, sequence iteration |
| `4-break-continue.py` | Loop Control | `break`, `continue`, loop termination |
| `4-oddeven.py` | Conditional Logic | Even/odd checks and branching |

### 2. **Functions & Modules** (Module 5)

| File | Purpose |
|------|---------|
| `5-functions.py` | Defining and calling functions, return values |
| `5-modules.py` | Importing modules and using shared utilities |
| `math_operations.py` | Mathematical helper functions |

### 3. **Network Programming** (Module 6)

| File | Purpose |
|------|---------|
| `networking/6-networking-client.py` | TCP client socket communication |
| `networking/6-networking-server.py` | TCP server socket communication |
| `networking/6-networking-request.py` | HTTP request handling example |
| `networking/6-networking-scap.py` | Packet analysis with Scapy |
| `sockets/client.py` | Socket client implementation |
| `sockets/server.py` | Socket server implementation |
| `sockets/soc.py` | Socket utilities and helpers |

### 4. **API & Automation Examples**

| File | Purpose |
|------|---------|
| `apis/api-ex.py` | HTTP GET request example using `requests` |
| `apis/api-req.py` | HTTP PUT and DELETE request examples |
| `automation/getlinks.py` | Web scraping with BeautifulSoup |
| `automation/par.py` | JSON parsing and manipulation |
| `automation/par2.py` | Additional parsing utilities |
| `automation/task_schedule.py` | Scheduled task execution with `schedule` |

### 5. **Database Automation**

| File | Purpose |
|------|---------|
| `python-postgres/postgres-python.py` | PostgreSQL connection and database automation using `psycopg2` |

---

## 🚀 Getting Started

### Prerequisites

- **Python:** 3.12 or higher
- **pip:** Python package manager
- **Virtual environment:** Recommended for dependency isolation

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd devops-python
   ```

2. Create and activate a virtual environment:
   ```bash
   python3.12 -m venv devops-python-venv
   source devops-python-venv/bin/activate  # Linux/macOS
   # or
   devops-python-venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install optional extras used by some examples:
   ```bash
   pip install beautifulsoup4 schedule psycopg2-binary
   ```

---

## 📖 Usage Examples

### Basic Python Examples

```bash
python 1-hello.py
python 2-fileread.py
python 5-functions.py
```

### API Examples

```bash
python apis/api-ex.py
python apis/api-req.py
```

### Automation Examples

```bash
python automation/getlinks.py
python automation/par.py
python automation/task_schedule.py
```

### PostgreSQL Example

```bash
python python-postgres/postgres-python.py
```

### Networking Examples

```bash
python networking/6-networking-server.py
python networking/6-networking-client.py
```

### Socket Programming Examples

```bash
python sockets/server.py
python sockets/client.py
```

---

## 📝 Module Details

### Fundamentals Breakdown

**Variables & Data Types**
- Integers, floats, strings
- Variable assignment and printing
- Basic expressions and formatting

**File Operations**
- Open, read, write, and close files
- File system checks
- Data persistence

**Control Structures**
- Conditional branching (`if`, `elif`, `else`)
- Iterative loops (`for`, `while`)
- Loop control with `break` and `continue`

**Functions**
- Defining reusable functions
- Passing arguments and returning values
- Reuse across scripts

**Modules**
- Built-in and custom module imports
- Encapsulation of shared logic
- Code organization and reuse

**API & Automation**
- REST API calls with `requests`
- JSON serialization and parsing
- HTML parsing with BeautifulSoup
- Task scheduling with `schedule`

**Database Automation**
- PostgreSQL connection management
- Query execution and result handling
- Database creation and metadata inspection

**Network Programming**
- TCP socket communication
- Server/client lifecycle management
- Data send/receive workflows
- Packet inspection with Scapy

---

## 🔧 Configuration

### Virtual Environment

The `devops-python-venv/` virtual environment contains:
- Python 3.12 interpreter
- pip package manager
- Standard build tools such as `setuptools` and `wheel`

### Recommended Packages

- `requests`
- `beautifulsoup4`
- `schedule`
- `psycopg2-binary`
- `scapy`

---

## 💡 Best Practices Demonstrated

✅ Modular code organization  
✅ Proper file handling  
✅ Function reuse and abstraction  
✅ API request workflows  
✅ JSON parsing and automation scripting  
✅ Scheduled task execution  
✅ PostgreSQL database automation  
✅ Socket-based network communication  
✅ Clean dependency and environment management

---

## 🎓 Recommended Learning Path

1. Start with `1-hello.py`
2. Continue through file I/O and control flow examples
3. Learn function and module structure in `5-functions.py` and `5-modules.py`
4. Practice API and automation flows in `apis/` and `automation/`
5. Explore sockets and networking scripts in `networking/` and `sockets/`
6. Review the database automation example in `python-postgres/postgres-python.py`

---

## 📚 Key Concepts Covered

| Concept | Files | Level |
|---------|-------|-------|
| Variables & Types | 1-hello.py | Beginner |
| File I/O | 2-fileread.py, 2-filewrite.py, 3-fileoperations.py | Beginner |
| Conditionals | 4-ifelse.py, 4-oddeven.py | Beginner |
| Loops | 4-loops.py, 4-break-continue.py | Beginner |
| Functions | 5-functions.py | Beginner |
| Modules | 5-modules.py, math_operations.py | Intermediate |
| HTTP APIs | apis/api-ex.py, apis/api-req.py | Intermediate |
| Automation | automation/*.py | Intermediate |
| PostgreSQL | python-postgres/postgres-python.py | Intermediate |
| Networking | networking/*, sockets/* | Intermediate |

---

## ⚠️ Important Notes

- Ensure `arjun.txt` exists for file I/O examples.
- Run server scripts before client scripts in networking examples.
- Update PostgreSQL credentials in `python-postgres/postgres-python.py` before execution.
- Install optional packages when using BeautifulSoup, scheduling, or PostgreSQL examples.
- Some network and Scapy examples may require elevated permissions.

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Activate virtual environment and install dependencies |
| `FileNotFoundError` | Confirm the working directory and file path |
| `ConnectionRefusedError` | Start the network server before the client |
| PostgreSQL connection error | Verify host, port, user, and password |
| Permission denied | Use a non-privileged port or run with elevated privileges |

---

## 📖 Additional Resources

- [Python Documentation](https://docs.python.org/3.12/)
- [Requests Documentation](https://docs.python-requests.org/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [Socket Programming Guide](https://docs.python.org/3.12/library/socket.html)

---

## ✍️ Author

**Arjun**  
DevOps Python Learning Project

---

## 📄 License

This project is provided as-is for educational purposes.

---

**Last Updated:** May 2026  
**Status:** Active Learning Project
