# 🔄 Python Type Conversion

Type conversion is the process of converting a value from one data type to another.

Python provides several built-in functions for type conversion, allowing programs to work with data in the appropriate format.

This section demonstrates both **implicit** and **explicit** type conversion with practical Python examples.

---

## 📌 Types of Type Conversion

Python supports two main types of conversion:

1. **Implicit Type Conversion**
2. **Explicit Type Conversion**


## 📂 Files in This Section

```text
05-type-conversion/
│
├── README.md
├── implicit_conversion.py
├── explicit_conversion.py
├── numeric_conversion.py
├── string_conversion.py
├── boolean_conversion.py
└── type_conversion_with_input.py
```

| File | Description |
|---|---|
| `implicit_conversion.py` | Demonstrates automatic type conversion |
| `explicit_conversion.py` | Demonstrates manual type conversion |
| `numeric_conversion.py` | Converts between numeric types |
| `string_conversion.py` | Demonstrates conversion to strings |
| `boolean_conversion.py` | Demonstrates truthy and falsy values |
| `type_conversion_with_input.py` | Demonstrates conversion of user input |

---

## 🎯 Learning Objectives

After completing this section, I understand how to:

- Distinguish between implicit and explicit type conversion
- Convert strings into numeric values
- Convert between numeric types
- Convert values into strings
- Understand Boolean conversion
- Work with truthy and falsy values
- Convert user input into appropriate data types
- Recognize invalid type conversions

---

## 💡 Key Takeaways

- Python can perform some type conversions automatically.
- Explicit conversion is performed using built-in functions such as `int()`, `float()`, `str()`, and `bool()`.
- `input()` always returns a string.
- Type conversion is often necessary before performing calculations with user input.
- `int()` truncates the fractional part of a float rather than rounding it.
- Empty values such as `""`, `[]`, `{}`, and `None` are generally falsy.
- Invalid conversions can raise exceptions such as `ValueError`.

---
