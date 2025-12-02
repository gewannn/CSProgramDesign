from random import *  # 为了随机数，这个库必须要有

def CreatePassword():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "~!@#$%^&*?"
    all = lower + upper + digits + specials
    length = randint(8, 17)
    password = [
        choice(lower),
        choice(upper),
        choice(digits),
        choice(specials)]
    for i in range(length - 4):
        password.append(choice(all))
    shuffle(password)
    return "".join(password)

for i in range(10):
    print(CreatePassword())