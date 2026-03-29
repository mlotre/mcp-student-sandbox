# MCP Student Sandbox

This is a collection of Python scripts demonstrating various programming concepts, bugs, and fixes in a student learning environment.

## Files

- **failing_calculator.py**: Contains a function to calculate average ratios, with a fix for zero division errors.
- **mystery_module.py**: Solves quadratic equations using the quadratic formula. The `fn_x(a, b, c)` function computes the roots of the equation ax² + bx + c = 0.
- **secret_leak.py**: Demonstrates a security vulnerability with a hardcoded secret key (for educational purposes only).
- **spaghetti_logic.py**: Refactored code showing clean code principles with modular functions for data processing.

## Usage

Run any Python file using `python filename.py` in the terminal.

For `mystery_module.py`, you can import and use `fn_x` to solve quadratic equations:

```python
from mystery_module import fn_x
roots = fn_x(1, -3, 2)  # Solves x² - 3x + 2 = 0
print(roots)  # Output: (2.0, 1.0)
```

## Notes

- Ensure Python 3 is installed.
- The scripts are for educational purposes; handle secrets securely in real applications.