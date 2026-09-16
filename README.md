# Task 3: Password Generator

## Project Overview

A Python command-line Password Generator developed as part of the 
Decodelabs Internship. It creates a random password using uppercase and
lowercase letters, digits, and special characters.

## Objective

To practice Python modules, functions, random selection, strings, user
input, validation, and exception handling.

## Features

-   Custom password length
-   Uppercase and lowercase letters
-   Numbers
-   Special characters
-   Random password generation
-   Password-length validation
-   Invalid-input handling

## Technologies Used

-   Python 3
-   `random` module
-   `string` module
-   Command Line Interface (CLI)

## Methodology

1.  Import `random` and `string`.
2.  Build a character pool from letters, digits, and punctuation.
3.  Ask the user for password length.
4.  Validate the length.
5.  Use `random.choice()` to select random characters.
6.  Join the selected characters into the password.
7.  Display the generated password.

## Code Review and Improvements

The original uploaded code already used `random.choice()` with lowercase
letters, uppercase letters, numbers, and special characters.
fileciteturn3file0L3-L17

The reviewed version improves it by: - Using `string` constants for
cleaner character handling - Creating a reusable `generate_password()`
function - Adding a `main()` entry point - Validating password length -
Handling non-numeric input safely - Improving CLI presentation and
messages

## How to Run

``` bash
python password_generator.py
```

Enter a password length of 4 or more.

## Example Output

``` text
===================================
       PASSWORD GENERATOR
===================================
Enter password length (minimum 4): 12

Password generated successfully!
Your password: aB7@kP2#xL9!
```

The actual password will be different each time because characters are
selected randomly.

## Screenshots

Add screenshots showing: - Successfully generated password - Another
generated password - Invalid input or length handling

## Project Structure

``` text
Task-4-Password-Generator/
├── password_generator.py
├── screenshots/
│   ├── generated_password.png
│   ├── another_password.png
│   └── invalid_input.png
├── report/
│   └── Password_Generator_Report.pdf
└── README.md
```

## Result

The application successfully generates random passwords according to the
length specified by the user.

## Conclusion

This project demonstrates practical Python programming through modules,
functions, random selection, strings, input validation, and exception
handling.
