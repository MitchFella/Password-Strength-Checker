# Password Strength Checker

This Python script evaluates the strength of a password based on its **length**, **character diversity**, and whether it appears in a list of **common passwords**.

---

## Features

- Checks if a password exists in a list of common passwords
- Scores password length (up to 4 points)
- Scores character diversity:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- Outputs a total score and strength label

---

## Scoring

### Length (Max 4 points)
- +1 point for each threshold met:
  - 8 characters
  - 12 characters
  - 16 characters
  - 20 characters

### Character Diversity (Max 3 points)
- +1 point for each additional character type beyond one

### Common Password Check
- If the password appears in the common password list, the score is **0** and the program exits immediately

### Total Score
- Range: **0–7**

---

## Strength Levels

| Score | Strength      |
|------:|---------------|
| 0–2   | Weak          |
| 3–4   | Moderate      |
| 5     | Strong        |
| 6–7   | Very Strong   |

---

## Usage

1. Place the file  
   `10-million-password-list-top-10000.txt`  
   in the **same directory** as the script.

2. Edit the `password` variable inside the script to test different passwords.

3. Run the script:
   ```bash
   python password_strength_checker.py

Password Analysis:
Length: 12
Character types: 4 (Uppercase, Lowercase, Digits, Special characters)
Score: 7/7
Password strength: Very Strong


