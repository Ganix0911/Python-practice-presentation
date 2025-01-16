
string = input("Enter a string: ")

def length_of_string(string):
    count = 0
    for i in string:
        count += 1
    return count
print(length_of_string(string))


