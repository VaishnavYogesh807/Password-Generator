import random
import string
import time
import os

os.path.join(os.path.dirname(__file__))

os.chdir("/Users/vaishnav/Library/Mobile Documents/com~apple~CloudDocs/Python/")

with open("top_english_nouns_lower_100000.txt") as f:
    WORDS = f.read().splitlines()

def memorable_password(n, case):

    chosen_words = random.sample(WORDS, n)
    result = []

    for word in chosen_words:

        num = random.randint(0, 9)

        if case == 'upper':
            word = word.capitalize()
        elif case == 'lower':
            word = word.lower()

        result.append(word + str(num))
    
    return "-".join(result)

def random_password(n, punct, char):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    if punct:
        characters += string.punctuation

    for c in char:
        characters = characters.replace(c, "")

    #for i in range(n):
        #return''.join(random.choice(characters))
    
    return ''.join(random.choice(characters) for _ in range(n))

def log_password(folder, password):
    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, "Generated_Passwords.txt")

    with open(path, "a") as f:
        f.write(f"[{time.ctime()}] {password}\n")

for _ in range(1000):
    pass_type = random.choice(["memorable", "random"])

    if pass_type == "memorable":
        pw = memorable_password(3, "upper")
        log_password("Memorable", pw)
    else:
        pw = random_password(10, True, "l1O0")
        log_password("Random", pw)
