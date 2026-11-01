# Password Strength Checker

A Python-based cybersecurity project that evaluates password strength using password length and character diversity.

**Part of the DecodeLabs Cyber Security Industrial Training Program — Week 1, Batch 2026.**

[**View GitHub Repository**](https://github.com/arfahabib123/DecodeLabs-Week1-Password-Strength-Checker)

---

## Project Overview

The **Password Strength Checker** is a Python-based cybersecurity project developed as part of the DecodeLabs Cyber Security Industrial Training Kit (Project 1).

The application evaluates password strength by checking its length and character variety, including uppercase letters, lowercase letters, numbers, and special symbols. Based on these checks, it classifies passwords as **WEAK**, **MEDIUM**, or **STRONG**.

## Learning Objectives

- Understand the importance of password security.
- Learn Python string handling and conditional statements.
- Identify uppercase letters, lowercase letters, digits, and special symbols.
- Apply basic password-strength evaluation techniques.
- Practice writing and running unit tests.

## Features

- Checks minimum password length.
- Detects uppercase and lowercase letters.
- Identifies numeric digits.
- Detects special characters.
- Calculates a password-strength score.
- Classifies passwords as WEAK, MEDIUM, or STRONG.
- Provides feedback for improving weak passwords.
- Includes automated unit tests.

## Technologies Used

- **Programming Language:** Python
- **Python Modules:** `string`, `sys`, `unittest`
- **Code Editor:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub

## Project Structure

```text
DecodeLabs-Week1-Password-Strength-Checker/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_password.py
│
├── README.md
├── .gitignore
└── LICENSE
```

## Password Evaluation Criteria

The application evaluates passwords using the following criteria:

1. Minimum password length of 8 characters.
2. Presence of uppercase letters.
3. Presence of lowercase letters.
4. Presence of numeric digits.
5. Presence of special symbols.
6. Additional score for passwords containing at least 12 characters.

## Strength Classification

| Classification | Score |
|---|---|
| WEAK | Below 3 |
| MEDIUM | 3 |
| STRONG | 4 or above |

Passwords shorter than 8 characters are automatically classified as WEAK.

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/arfahabib123/DecodeLabs-Week1-Password-Strength-Checker.git
```

### 2. Navigate to the Project Directory

```bash
cd DecodeLabs-Week1-Password-Strength-Checker
```

### 3. Run the Application

```bash
python src/main.py
```

## Running Unit Tests

Run the following command from the main project directory:

```bash
python -m unittest discover -s tests -v
```

The project includes 10 automated tests to verify password evaluation, character detection, scoring, and strength classification.

## Learning Outcomes

Through this project, I practiced:

- Python programming fundamentals.
- String handling and conditional logic.
- Basic cybersecurity and password security concepts.
- Modular code organization.
- Unit testing and debugging.
- Git and GitHub project management.

## Future Improvements

- Add checks against commonly used passwords.
- Include checks for known compromised passwords.
- Improve password input privacy.
- Introduce a graphical user interface.
- Expand password security evaluation criteria.

## Disclaimer

This project is developed for educational purposes as part of cybersecurity training. It demonstrates basic password-strength evaluation and is not a complete password-security auditing solution.

## Author

**Arfa Habib**

DecodeLabs Cyber Security Industrial Training Program — Batch 2026

[GitHub Profile](https://github.com/arfahabib123)