def calculate_length(string):
    """Calculate the length of a string."""
    return len(string)

def count_characters(string):
    """Count the number of characters in a string."""
    return len(string)

def replace_first_char(string):
    """Replace all occurrences of the first character with '$' except the first occurrence."""
    first_char = string[0]
    return first_char + string[1:].replace(first_char, '$')

def swap_and_concatenate(string1, string2):
    """Swap the first two characters of each string and concatenate them with a space."""
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]
    return new_string1 + " " + new_string2

def concatenate_four_strings(s1, s2, s3, s4):
    """Concatenate four variables with spaces."""
    return s1 + " " + s2 + " " + s3 + " " + s4

def concatenate_input_strings():
    """Get two strings from user input and concatenate them."""
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    return string1 + " " + string2

def create_paragraph(name, age):
    """Concatenate name and age into a paragraph."""
    return f"My name is {name} and I am {age} years old."

# Example usage
string = "hello"
print(f"Length of '{string}': {calculate_length(string)}")
print(f"Number of characters in '{string}': {count_characters(string)}")
print(f"String after replacing first char occurrences: {replace_first_char(string)}")

string1 = "hello"
string2 = "world"
print(f"Swapped and concatenated: {swap_and_concatenate(string1, string2)}")

s1, s2, s3, s4 = "Python", "is", "a", "language"
print(f"Concatenated strings: {concatenate_four_strings(s1, s2, s3, s4)}")

# For input-based concatenation
print(f"User concatenated strings: {concatenate_input_strings()}")

# Concatenating name and age
name = "Charles"
age = 22
print(create_paragraph(name, age))