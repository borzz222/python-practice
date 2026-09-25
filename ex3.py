import string
import random
letters = random.choices(string.ascii_uppercase, k=3)
digits = random.choices(string.digits, k=3)
specials = random.choices("!@X#$%^&*", k=2)
password = letters + digits + specials
random.shuffle(password)
print("".join(password))
