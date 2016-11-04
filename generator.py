import sys
import string
import random

def generate():
    num = "0"
    size = raw_input("Enter a password length: ")
    try:
        int(size)
    except ValueError:
        num = "error"
        print("The size you picked (%s) is not an integer." % size)
    else:
        size = int(size)
        if size < 8:
            num = "error"
            if size < 0:
                print("The size you picked (%s) is not positive." % size)
            else:
                print("The size you picked (%s) is too small." % size)
        elif size >= 8 and size < 300000:
            num = "1"
            num = random.choice(string.ascii_letters)
            for i in range(0, size):
                n = random.randint(0,4)
                if n == 0 or n == 3:
                    num += random.choice(string.ascii_letters)
                elif n == 1 or n == 4:
                    num += str(random.randint(0,9))
                elif n == 2:
                    num += random.choice(string.punctuation)
        elif size >= 300000:
            num = "error"
            print("The size you picked (%s) is too large to be calculated in 1 second." % size)

    return num
