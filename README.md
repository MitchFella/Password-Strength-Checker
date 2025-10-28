## Password-Strength-Checker
# This Python script evaluates the strength of a password based on its length, character diversity, and whether it appears in a list of common passwords.
#
# Features
# 
# Checks if a password is in a list of common passwords
# 
# Scores password length (up to 4 points)
# 
# Scores character diversity (uppercase, lowercase, # digits, special characters)
# 
# Outputs a total score and strength label
# 
# Scoring
# Criteria	Description	Max Points
# Length	+1 for each threshold: 8, 12, 16, 20 # characters	4
# Character diversity	+1 for each additional character # type beyond one	3
# Common password	Automatically scores 0 and exits	—
# Total	0–7	—
# Strength Levels
# Score	Strength
# 0–2	Weak
# 3–4	Moderate
# 5	Strong
# 6–7	Very Strong
# Usage
# 
# Place the file 10-million-password-list-top-10000.txt # in the same directory as the script.
# 
# Edit the password variable inside the script to test # different passwords.
# 
# Run the script with:
# 
# python password_strength_checker.py
# 
# 
# Example output:
# 
# Password Analysis:
# Length: 12
# Character types: 4 (Uppercase Lowercase Digits Special # chars)
# Score: 7/7
# Password strength: Very Strong