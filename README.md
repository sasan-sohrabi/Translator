
# Translator Project 🌐

![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This Python project demonstrates the use of function and class decorators to translate text between different languages. The decorators leverage the `translators` library, which provides access to popular translation services such as Google Translate. The project showcases flexible translation configurations using decorators both with and without parameters.

## 🗂 Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Function-based Decorator (No Parameters)](#function-based-decorator-no-parameters)
  - [Function-based Decorator (With Parameters)](#function-based-decorator-with-parameters)
  - [Class-based Decorator](#class-based-decorator)
- [Examples](#examples)
- [License](#license)

## 🔧 Project Structure

The project is divided into three parts:

1. **Function-based Decorator Without Parameters**: Translates text from English to Persian using Google Translate.
2. **Function-based Decorator With Parameters**: Translates text using customizable parameters for the translation provider and languages.
3. **Class-based Translation Decorators**: Demonstrates class-based decorators for translation with and without parameters.

## 📋 Requirements

- Python 3.x
- `translators` Python library

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/translator_project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd translator_project
   ```
3. Install the dependencies:
   ```bash
   pip install translators
   ```

## 💡 Usage

### Function-based Decorator (No Parameters)

This decorator translates English text to Persian by default using Google Translate.

```python
@first_translator
def first_original_text(text: str) -> str:
    return text

test_text = "apple cat"
print(first_original_text(test_text))
```

### Function-based Decorator (With Parameters)

This decorator allows you to specify the translation provider and languages using parameters.

```python
@prefix_translator(provider='google', from_language='auto', to_language='fa')
def second_original_text(text: str) -> str:
    return text

test_text = "apple"
print(second_original_text(test_text))
```

### Class-based Decorator

You can use class-based decorators to achieve more flexibility in your translation logic.

```python
# Class-based decorator without parameters
@ThirdTranslator1
def third_first_original_text(text: str) -> str:
    return text

test_text = "apple cat"
print(third_first_original_text(test_text))

# Class-based decorator with parameters
@ThirdTranslator2(provider='google', from_language='auto', to_language='tr')
def third_second_original_text(text: str) -> str:
    return text

test_text = "apple cat"
print(third_second_original_text(test_text))
```

## 🔍 Examples

You can modify the text or languages in these examples to fit your needs:

1. **Simple Translation from English to Persian**:
    ```python
    test_text = "apple cat"
    print(first_original_text(test_text))  # Translates to Persian
    ```

2. **Translation with Custom Provider and Language**:
    ```python
    test_text = "apple"
    print(second_original_text(test_text))  # Translates to Persian
    ```

3. **Class-based Translation to Turkish**:
    ```python
    test_text = "apple cat"
    print(third_second_original_text(test_text))  # Translates to Turkish
    ```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
