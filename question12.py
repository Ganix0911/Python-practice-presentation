
string = input("Enter a string: ")

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False