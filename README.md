# GenAI Task 5 - Utility and Shop Package

This project demonstrates basic Python utility modules and a small shopping-related package. It includes arithmetic helpers, string processing functions, and discount/billing calculations.

## Project Structure

- [main.py](main.py) - example script that imports and runs all utility functions
- [math_utils.py](math_utils.py) - mathematical helper functions
- [string_utils.py](string_utils.py) - string processing helpers
- [shop_package/__init__.py](shop_package/__init__.py) - package exports
- [shop_package/billing.py](shop_package/billing.py) - total and tax calculations
- [shop_package/discount.py](shop_package/discount.py) - discount-related functions

## Features

### Math utilities
- `add(a, b)`
- `subtract(a, b)`
- `square(a)`

### String utilities
- `capitalize_word(text)`
- `reverse_string(text)`
- `word_count(text)`

### Shop package
- `calculate_total(prices)`
- `apply_tax(amount)`
- `apply_discount(price, percent)`
- `flat_discount(price)`

## Running the project

From the project root, run:

```bash
python main.py
```

This will print examples of each function in use.

## Example output

```python
30
10
100
Hello
olleh
2
90.0
50
600
```

## Notes

This is a small educational project intended to practice Python modules, package imports, and function-based calculations.
