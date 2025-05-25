# project2

This project contains a simple Python package with the following structure:

```
project2/
├── src/
│   ├── __init__.py
│   └── mian.py
└── README.md
```

## Files

- **src/__init__.py**
  
  ```python
  def main() -> None:
      print("Hello from project2!")
  ```

- **src/mian.py**
  
  ```python
  def main():
      print("Hello")

  if __name__ == "__main__":
      main()
      print("Pakistan zinda bad")
  ```

## Usage

To run the script:

```bash
python src/mian.py
```

This will output:

```
Hello
Pakistan zinda bad
```