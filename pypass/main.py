import string
import sys

password = "P@ssw0rd123!"

# Character type checks
upper_case = any(c in string.ascii_uppercase for c in password)
lower_case = any(c in string.ascii_lowercase for c in password)
digit = any(c in string.digits for c in password)
special_char = any(c in string.punctuation for c in password)

# Count of different character types
characters = [upper_case, lower_case, special_char, digit]
char_types = sum(characters)

# Base score
score = 0

# Check if password is common
with open("10-million-password-list-top-10000.txt", "r") as f:
    common_passwords = f.read().splitlines()

if password in common_passwords:
    print("Common password detected. Strength score: 0/7")
    sys.exit()  # Correct way to exit

# --- Length scoring ---
len_password = len(password)
if len_password >= 8:
    score += 1
if len_password >= 12:
    score += 1
if len_password >= 16:
    score += 1
if len_password >= 20:
    score += 1

# --- Character diversity scoring ---
if char_types > 1:
    score += 1
if char_types > 2:
    score += 1
if char_types > 3:
    score += 1

# --- Feedback ---
print(f"\nPassword Analysis:")
print(f"Length: {len_password}")
print(f"Character types: {char_types} ({'Uppercase' if upper_case else ''} "
      f"{'Lowercase' if lower_case else ''} "
      f"{'Digits' if digit else ''} "
      f"{'Special chars' if special_char else ''})")
print(f"Score: {score}/7")

# --- Strength label ---
if score < 3:
    strength = "Weak"
elif 3 <= score < 5:
    strength = "Moderate"
elif 5 <= score < 6:
    strength = "Strong"
else:
    strength = "Very Strong"

print(f"Password strength: {strength}")

exit()  

