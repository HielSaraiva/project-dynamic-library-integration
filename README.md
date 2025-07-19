# Dynamic Library Integration: C and Python Interoperability

This project demonstrates the creation of a dynamic library (.dylib) in C and its utilization in Python through CFFI (C Foreign Function Interface). The implementation showcases a function that generates random descriptions for football players.

**Academic Context**: This project was developed for the Operating Systems course as part of university curriculum, demonstrating inter-language communication and dynamic library concepts.

## Table of Contents

- [Project Description](#-project-description)
- [Project Structure](#️-project-structure)
- [Technologies Used](#️-technologies-used)
- [Prerequisites](#-prerequisites)
- [Step-by-Step Implementation](#-step-by-step-implementation)
- [Quick Execution Commands](#-quick-execution-commands)
- [How It Works](#-how-it-works)
- [Demonstrated Concepts](#-demonstrated-concepts)
- [Platform-Specific Notes](#-platform-specific-notes)
- [References](#-references)

## 📋 Project Description

The project consists of:
- **C Code**: Core function implementation for generating random player descriptions
- **Dynamic Library**: C function exported as platform-specific dynamic library
- **Python Interface**: High-level interface utilizing the C library through CFFI

## 🏗️ Project Structure

```
projeto-dll/
├── README.md
├── c_code/
│   ├── jogador.c        # C function implementation
│   ├── main.c           # C test program
│   ├── main             # C executable
│   └── libjogador.dylib # Dynamic library (macOS)
└── py_code/
    ├── .venv/           # Python virtual environment
    ├── main.py          # Python main script
    ├── libjogador.dylib # Library copy for Python
    └── requirements.txt # Python dependencies
```

## 🛠️ Technologies Used

- **C**: Low-level implementation language
- **Python 3.13+**: High-level interface language
- **CFFI**: C Foreign Function Interface library
- **GCC/Clang**: Compiler for C code and dynamic library generation

## 📦 Prerequisites

- GCC (Clang on macOS)
- Python 3.13+
- pip (Python package manager)

## 🚀 Step-by-Step Implementation

### 1. C Code Development

#### 1.1. Create the core function (`jogador.c`)
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void descreve_jogador(const char* nome) {
    const char* adjetivos[] = {
        "bagre", "ligeiro", "cabuloso", "letal", "encapetado",
        "matuto veloz", "bicho ruim", "canhoto do além",
        "motorzinho da bola", "tenebroso"
    };

    int total = sizeof(adjetivos) / sizeof(adjetivos[0]);
    srand((unsigned int)time(NULL));
    int indice = rand() % total;

    printf("O %s é %s.\n", nome, adjetivos[indice]);
}
```

#### 1.2. Create test program (`main.c`)
```c
#include <stdio.h>

void descreve_jogador(const char* nome);

int main(void) {
   descreve_jogador("Marinho");
   return 0;
}
```

### 2. C Code Compilation and Testing

#### 2.1. Compile and test the C program
```bash
cd c_code
gcc main.c jogador.c -o main
./main
```

**Expected output:**
```
O Marinho é [random adjective].
```

### 3. Dynamic Library Creation

#### 3.1. Generate the dynamic library
```bash
cd c_code
gcc -dynamiclib -o libjogador.dylib jogador.c
```

**Parameters:**
- `-dynamiclib`: Creates a dynamic library (macOS specific)
- `-o`: Specifies output file name

**Alternative command (also works on macOS):**
```bash
gcc -shared -fPIC jogador.c -o libjogador.dylib
```

### 4. Python Environment Setup

#### 4.1. Create virtual environment
```bash
cd py_code
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

#### 4.2. Install dependencies
```bash
pip install cffi
pip freeze > requirements.txt
```

#### 4.3. Copy library to Python directory
```bash
cp ../c_code/libjogador.dylib ./
```

### 5. Python Interface Development

#### 5.1. Create main script (`main.py`)
```python
from cffi import FFI

ffi = FFI()

# C function declaration
ffi.cdef("""
    void descreve_jogador(const char* nome);
""")

# Load dynamic library
lib = ffi.dlopen("./libjogador.dylib")

# Call function with player name
nome = "Lucero"
lib.descreve_jogador(nome.encode("utf-8"))
```

### 6. Project Execution

#### 6.1. Execute via Python
```bash
cd py_code
source .venv/bin/activate
python main.py
```

**Expected output:**
```
O Lucero é [random adjective].
```

## 🔧 Quick Execution Commands

### C Compilation and Testing
```bash
# Navigate to C directory
cd c_code

# Compile test program
gcc main.c jogador.c -o main

# Execute test
./main

# Generate dynamic library
gcc -dynamiclib -o libjogador.dylib jogador.c
```

### Python Setup and Execution
```bash
# Navigate to Python directory
cd py_code

# Activate virtual environment
source .venv/bin/activate

# Install dependencies (if needed)
pip install -r requirements.txt

# Copy library (if needed)
cp ../c_code/libjogador.dylib ./

# Execute application
python main.py
```

## 🧪 How It Works

1. **C Function**: `descreve_jogador()` receives a name and generates a random description
2. **Dynamic Library**: Function is compiled as platform-specific dynamic library for runtime loading
3. **CFFI**: Python interface that enables loading and executing C code
4. **Integration**: Python calls C function passing parameters and receiving results

## 🎯 Demonstrated Concepts

- **Language Interoperability**: Integration between different programming languages
- **Dynamic Libraries**: Creation and usage of shared code modules
- **FFI (Foreign Function Interface)**: Calling native code from high-level languages
- **Modularization**: Separation of concerns between languages
- **Operating Systems Concepts**: Dynamic linking and library loading mechanisms

## 🖥️ Platform-Specific Notes

### Dynamic Library Extensions by Platform:
- **macOS**: `.dylib` (Dynamic Library) - Used in this project
- **Linux**: `.so` (Shared Object)
- **Windows**: `.dll` (Dynamic Link Library)

### Compilation Commands by Platform:

#### macOS (Used in this project):
```bash
gcc -dynamiclib -o libjogador.dylib jogador.c
# or
gcc -shared -fPIC jogador.c -o libjogador.dylib
```

#### Linux:
```bash
gcc -shared -fPIC jogador.c -o libjogador.so
```

#### Windows (MinGW):
```bash
gcc -shared jogador.c -o libjogador.dll
```

**Note**: This project was specifically developed and tested on macOS with Apple Silicon, hence the use of `.dylib` extension.

## 📚 References

- [CFFI Documentation](https://cffi.readthedocs.io/)
- [GCC Manual - Shared Libraries](https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html)
- [Python C Extension Programming](https://docs.python.org/3/extending/)
- [Dynamic Libraries on macOS](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/)

---

**Development Environment**: This project was developed and tested on macOS with Apple Silicon. Commands and library extensions may vary on different operating systems (Linux uses `.so`, Windows uses `.dll`).