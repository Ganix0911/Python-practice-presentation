
string = input("Enter a string: ")

def reverse_string(string):
    return string[::-1]
print(reverse_string(string))

def skip_letters(string):
    return string[::2]
print(skip_letters(string))