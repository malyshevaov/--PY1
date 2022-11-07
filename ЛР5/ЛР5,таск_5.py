import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

def get_random_password() -> str:
    str_ = ascii_uppercase, ascii_lowercase, digits
    str_ = "".join(str_)
    password = (random.sample(str_,8))
    return "".join(password)
print(get_random_password())
