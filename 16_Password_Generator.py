import random
import string

def pwGene(n):
    #count = 1
    count = 3
    while (count != 4):
        schr = "!@#$%^&*()?"
        pw = []
        for _ in range(n):
            a = chr(random.randint(65, 90))
            b = chr(random.randint(97, 122))
            c = chr(random.randint(48, 57))
            pw.append(random.choice([a, b, c]))
        pw = "".join(pw)
        #print (str(count) + ": " + pw)
        count += 1
    return pw

n = int(input("How long do you want for your password? "))
password = pwGene(n)
#choice = int(input("What password do you choose: "))
print ("Own password: " + password)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated Password:", generate_password(n))
