#!/usr/bin/env python

"""passwordgen.py: Generates password based on length passed"""

__author__ = "Vick Kumar"
__email__ = "vick.kumar@proton.me"
__copyright__ = "Copyright 2022, GNU General Public License v3.0"
__license__ = "GPL"
__version__ = "0.0.1"

import sys
import string
import random

def main():
    try:
        if len(sys.argv[1]):
            try:
                length = int(sys.argv[1])
                if length >= 8:
                    print(generate(length))
                else:
                    print("The length should be greater or equal to 8, here's a free one: " + generate(8))
            except ValueError:
                print("An integer was not passed, try again. \n Usage: passwordgen.py 32")
    except:
        print("You did not pass an integer for length of password, try again.\n Usage: passwordgen.py 32")

def generate(length):
    password = []
    for i in range(length):
        choices = string.ascii_letters + string.digits + string.punctuation
        randomchar = random.choice(choices)
        password.append(randomchar)
    return "".join(password)


if __name__ == "__main__":
    main()
