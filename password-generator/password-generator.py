import string
import random

length = input("Please enter length of password: ")
length_converted = int(length)


def randomString(string_length=length_converted):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))


print ("Random String is ", randomString())



