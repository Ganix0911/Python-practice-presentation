#Given a string, count how many vowels (a, e, i, o, u) it contains

string = input("Enter a string: ")

def count_vowels(string):
    count = 0
    for i in string:
        if i in "aeiou":
            count += 1
    return count

print(count_vowels(string))