from pathlib import Path
from os import sys

path = Path("chapter_10/reading_from_a_file/pi_million_digits.txt")
# path = Path("pi_million_digits.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
    sys.exit()

pi_string = ""
for line in contents.splitlines():
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
