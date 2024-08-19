import string
import random

num = string.digits
str_low = string.ascii_lowercase
str_up = string.ascii_uppercase
symbol = string.punctuation

password_1 = random.sample(str_up, 2)
password_2 = random.sample(str_low, 4)
password_3 = random.sample(num, 3)
password_4 = random.sample(symbol, 2)

password = password_1 + password_2 + password_3 + password_4

print("".join(password))
