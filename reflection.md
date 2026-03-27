# Developer Journal: Reflection on Mini-Project 2 BY SIFAN AYANO

# 1. Object-Oriented Programming and Inheritance
Course Connection: Classes, Objects, and Inheritance.

In this project, I implemented Inheritance by creating a ProHorse class that extends the base Horse class. Instead of rewriting the entire logic for a faster horse, I inherited the base attributes and only modified the get_speed method making the code easier to maintain.

# 2. Input Validation and Defensive Programming
Course Connection: User Input, String Manipulation, and Regular Expressions.

I enhanced the validate_bet function to handle real-world user behavior, such as including currency symbols which I have been using £. I used the re (Regular Expression) module with a specific pattern to ensure data integrity.

# 3. Automated Testing
Course Connection: Software Testing and Quality Assurance.

I used the pytest framework to verify that my validation logic was robust. I wrote test cases in test_race.py that check for multiple scenarios: a plain number, a number with a symbol, and invalid text. Running tests via the terminal was essential for catching bugs early.

# 4. File Handling
Course Connection: File Handling (Open, Read, Write).

The project required saving race results to an external file. I used Python's open command in append mode. This allows the tournament history to grow over time rather than overwriting the previous race results every time a new game starts the test results are saved in results.txt

# 5. Challenges and Problem Solving
I encountered a ModuleNotFoundError when running tests initially. I resolved this by learning how to run pytest as a module from the main directory. I also managed indentation and syntax issues in the validators file, which improved my understanding of Python structure.
