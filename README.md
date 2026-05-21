# DevOps Python Learning Repository

## Overview

A comprehensive collection of Python fundamentals and advanced networking examples designed for DevOps automation professionals. This repository serves as a learning resource covering core Python concepts, file I/O operations, control flow, functions, modules, and network programming with socket implementations.

**Target Audience:** DevOps Engineers, System Administrators, and Python Developers  
**Skill Level:** Beginner to Intermediate  
**Python Version:** 3.12+

---

## 📋 Project Structure

```
devops-python/
├── 1-hello.py                    # Basic Python syntax and data types
├── 2-fileread.py                 # File reading operations
├── 2-filewrite.py                # File writing operations
├── 3-fileoperations.py           # Advanced file manipulation
├── 4-ifelse.py                   # Conditional statements
├── 4-loops.py                    # Loop structures (for/while)
├── 4-break-continue.py           # Loop control flow
├── 4-oddeven.py                  # Conditional logic example
├── 5-functions.py                # Function definition and usage
├── 5-modules.py                  # Module imports and reusability
├── math_operations.py            # Mathematical utility module
├── networking/                   # Network programming examples
│   ├── 6-networking-client.py    # TCP client implementation
│   ├── 6-networking-request.py   # HTTP request handling
│   ├── 6-networking-scap.py      # Network packet analysis
│   └── 6-networking-server.py    # TCP server implementation
├── sockets/                      # Advanced socket programming
│   ├── client.py                 # Socket client application
│   ├── server.py                 # Socket server application
│   └── soc.py                    # Socket utility functions
├── devops-python-venv/           # Virtual environment (Python 3.12)
├── arjun.txt                     # Sample data file
└── README.md                     # This file
```

---

## 🎯 Learning Modules

### 1. **Python Fundamentals** (Modules 1-4)

| File | Topic | Key Concepts |
|------|-------|--------------|
| `1-hello.py` | Basic Syntax | Variables, data types (int, str, float), print statements |
| `2-fileread.py` | File Reading | File handling, read operations, resource management |
| `2-filewrite.py` | File Writing | Creating/writing files, data persistence |
| `3-fileoperations.py` | File Management | Rename, delete, check existence operations |
| `4-ifelse.py` | Conditionals | If/elif/else statements, boolean logic |
| `4-loops.py` | Iteration | For and while loops, iteration patterns |
| `4-break-continue.py` | Flow Control | Loop control with break/continue statements |
| `4-oddeven.py` | Logic Application | Practical conditional logic |

### 2. **Functions & Modules** (Module 5)

| File | Purpose |
|------|---------|
| `5-functions.py` | Function definition, parameters, return values, practical examples |
| `5-modules.py` | Module imports, code reusability, namespace management |
| `math_operations.py` | Reusable mathematical utilities (add, subtract, multiply, divide) |

### 3. **Network Programming** (Module 6)

| File | Purpose |
|------|---------|
| `networking/6-networking-client.py` | TCP client socket communication |
| `networking/6-networking-server.py` | TCP server socket communication |
| `networking/6-networking-request.py` | HTTP request handling |
| `networking/6-networking-scap.py` | Network packet analysis with Scapy |
| `sockets/client.py` | Advanced client implementation |
| `sockets/server.py` | Advanced server implementation |
| `sockets/soc.py` | Socket utility functions |

---

## 🚀 Getting Started

### Prerequisites

- **Python:** 3.12 or higher
- **pip:** Package manager for Python
- **Virtual Environment:** Recommended for dependency isolation

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd devops-python
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Create virtual environment
   python3.12 -m venv devops-python-venv

   # Activate virtual environment
   source devops-python-venv/bin/activate  # Linux/macOS
   # or
   devops-python-venv\Scripts\activate  # Windows
   ```

3. **Install dependencies (if any):**
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   # For networking examples with Scapy:
   pip install scapy
   ```

---

## 📖 Usage Examples

### Running Basic Python Examples

```bash
# Run hello world example
python 1-hello.py

# Run file reading example
python 2-fileread.py

# Run functions example
python 5-functions.py
```

### Testing Module Imports

```bash
# Test module import functionality
python 5-modules.py
```

### Running Network Examples

```bash
# Terminal 1: Start server
python networking/6-networking-server.py

# Terminal 2: Run client
python networking/6-networking-client.py
```

### Using Socket Programming

```bash
# Start socket server
python sockets/server.py

# In another terminal, start client
python sockets/client.py
```

---

## 📝 Module Details

### Fundamentals Breakdown

**Variables & Data Types**
- Integers, floats, strings
- Variable assignment and manipulation
- Type conversions

**File Operations**
- Reading file contents
- Writing data to files
- File path manipulation
- Error handling

**Control Structures**
- Conditional branching (if/elif/else)
- Loop iteration (for/while)
- Loop control (break/continue)
- Logical operators

**Functions**
- Function definition and parameters
- Return statements
- Function calls and arguments
- Scope and namespace

**Modules**
- Importing modules
- Creating reusable code
- Namespace management
- Module-level functions

### Network Programming Features

**Socket Communication**
- TCP client-server architecture
- Socket creation and binding
- Connection handling
- Data transmission/reception

**HTTP Networking**
- HTTP request handling
- Request/response cycles
- URL operations

**Packet Analysis**
- Network packet inspection
- Protocol analysis with Scapy
- Traffic monitoring

---

## 🔧 Configuration

### Virtual Environment Structure

The included `devops-python-venv/` contains:
- **Python 3.12** interpreter
- **pip** package manager
- Pre-installed packages: setuptools, wheel, pip
- Optional: Scapy for network analysis

---

## 💡 Best Practices Demonstrated

✅ Modular code organization  
✅ Proper file handling with resource closure  
✅ Function reusability  
✅ Module imports for code organization  
✅ Error handling (division by zero checks)  
✅ Socket communication patterns  
✅ Configuration management (host/port definitions)

---

## 🎓 Learning Path

**Recommended progression:**

1. Start with `1-hello.py` - Understand basic syntax
2. Progress through modules 2-4 - Learn file operations and control flow
3. Complete module 5 - Master functions and modules
4. Explore networking - Understand network programming fundamentals
5. Experiment with sockets - Practice client-server architecture

---

## 📚 Key Concepts Covered

| Concept | Files | Difficulty |
|---------|-------|-----------|
| Variables & Types | 1-hello.py | Beginner |
| File I/O | 2-fileread.py, 2-filewrite.py, 3-fileoperations.py | Beginner |
| Conditionals | 4-ifelse.py, 4-oddeven.py | Beginner |
| Loops | 4-loops.py, 4-break-continue.py | Beginner |
| Functions | 5-functions.py | Beginner |
| Modules | 5-modules.py, math_operations.py | Intermediate |
| Networking | networking/*, sockets/* | Intermediate |

---

## 🔍 Sample Code Snippets

### File Reading
```python
file = open('arjun.txt', 'r')
content = file.read()
print(content)
file.close()
```

### Function Definition
```python
def greet(name):
    print(f"Hello, {name}!!!")

greet('arjun')
```

### Module Import
```python
import math_operations
result = math_operations.add(5, 6)
print(f"Result: {result}")
```

### Socket Client
```python
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))
client_socket.send("Hello Server!".encode('utf-8'))
```

---

## ⚠️ Important Notes

- **File Paths:** Ensure `arjun.txt` exists in the root directory when running file operation examples
- **Network Examples:** Require server to be running before starting client
- **Port Availability:** Default port 12345 must be available
- **Scapy:** Network packet analysis examples require appropriate permissions (may need sudo on Linux)

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure you're in the correct directory and virtual environment is activated |
| `FileNotFoundError` | Verify file paths are correct relative to script location |
| `ConnectionRefusedError` | Ensure server is running before starting client |
| `Permission denied (sockets)` | Run with elevated privileges or use non-privileged ports |

---

## 📖 Additional Resources

- [Python Official Documentation](https://docs.python.org/3.12/)
- [Socket Programming Guide](https://docs.python.org/3.12/library/socket.html)
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [DevOps with Python](https://www.packtpub.com/product/python-devops/)

---

## ✍️ Author

**Arjun**  
DevOps Python Learning Project

---

## 📄 License

This project is provided as-is for educational purposes.

---

## 🤝 Contributing

Contributions and improvements are welcome! Feel free to:
- Add more examples
- Improve documentation
- Suggest additional networking examples
- Report issues or bugs

---

**Last Updated:** May 2026  
**Status:** Active Learning Project  
**Maintenance:** Regular updates as learning progresses
