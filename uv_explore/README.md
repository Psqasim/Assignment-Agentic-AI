# Explore-UV Projects

This repository contains two simple Python projects demonstrating basic structure and entry points.

## Project 1: `exlsplore-uv`

**File:** `src/__init__.py`

```python
def main():
    print("Hello from exlsplore-uv!")

if __name__ == "__main__":
    main()
```

**Description:**  
Runs a simple script that prints a greeting from `exlsplore-uv`.

---

## Project 2

**File:** `src/__init__.py`

```python
def main() -> None:
    print("Hello from project2!")
    
**File:** `src/main.py`
def main():
    print("Hello")

if __name__ == "__main__":
    main()
    print("Pakistan zinda bad")
```

**Description:**  
Contains two `main` functions (the second one overrides the first). When run as a script, it prints:

```
Hello
Pakistan zinda bad
```

---

## How to Run

Navigate to each project's directory and run:

```bash
python -m src
```

---

## Requirements

- Python 3.x

---

## Notes

- Each project demonstrates a basic Python package structure.
- The entry point is defined in `src/__init__.py` for both projects.
- For best practices, avoid redefining functions with the same name in the same file.