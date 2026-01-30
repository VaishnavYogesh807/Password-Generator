# Password-Generator

**Description:**
  This project creates a password generator that can produce two types of passwords: Memorable & Random

**How to use:**
  The program asks the user which type of password they want.
  Memorable: The user is asked for the number of words and whether the words should be in title, upper, or lower case.
  Input Ex: (3, title)
  Result: Apple7-Train3-Cloud9
  
  Random: The user is asked for the number of characters, whether punctuation should be included, and if there are any characters that should not be used.
  Input Ex: (9, True, "0OLl")
  Result: aG7kP2!qZ

The program also records every generated password along with the exact date and time it was created. These passwords are automatically saved into files inside separate folders for memorable and random passwords.

Modules Used:
  Randomness
  String handling
  Time tracking
  File handling


CODE Acknowledgements:

Line 8: Suggested by Mr.X to help with loading the file.
Line 10-11: CHATGPT helped with how to load the words from a text file.
Line 42-43: Original code failed to produce intended output, which was then revised by ChatGPT on line 45.
Line 47-54: Gained an understanding of how to create folders and save results directly into them without having to create the folders manually, with guidance from ChatGPT.
