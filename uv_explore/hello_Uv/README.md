# hello_Uv

A simple Python project using [uv](https://github.com/astral-sh/uv) for environment management.

## Description

This project contains a basic script that prints a greeting message.

```python
def main():
    print("Hello from exlsplore-uv!")

if __name__ == "__main__":
    main()
```

## Setup

1. **Install [uv](https://github.com/astral-sh/uv):**
   ```bash
   pip install uv
   ```

2. **Create a virtual environment:**
   ```bash
   uv venv .venv
   ```

3. **Activate the environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Run the script:**
   ```bash
   python hello_Uv.py
   ```

## License

MIT