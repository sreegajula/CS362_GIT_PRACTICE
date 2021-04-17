import string
import random

def randompass(num):
    ascii_string = string.ascii_lowercase + string.digits + string.ascii_uppercase
    password = ''.join(random.choice(ascii_string) for i in range(num)) ## reference from pynative
    print(password)

