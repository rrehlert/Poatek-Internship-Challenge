txt = "Hello World"[::-1]


def invert_string(string):
    inverted_string =  string[::-1]
    return inverted_string

def check_palindrome(string, inverted_string):
    string = string.lower()                     #Convert strings to lower to avoid Uppercase conflicts
    inverted_string = inverted_string.lower()
    if string == inverted_string:
        return True
    else:
        return False

if __name__ == '__main__':
    while(True):
        string = input("Enter a string to check: (leave empty to exit) \n")
        if not string:
            print("No string was entered, finishing the program")
            break
        else:
            inverted_string =  invert_string(string)
            if check_palindrome(string, inverted_string):
                print(f"{string} is a palindrome \n")
            else:
                print(f"{string} is not a palindrome \n")