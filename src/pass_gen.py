from random import choice
from string import ascii_letters, digits, punctuation

def generate_pass(length=10, chars=ascii_letters+digits+punctuation):
    pass_list = []
    for i in range(length):
        pass_list.append(choice(chars))
    return ''.join(pass_list)

print(generate_pass(8, ascii_letters+digits+punctuation))