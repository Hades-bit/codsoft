import random
import string

n=int(input('Enter the number of Characters: '))

Char_list=(string.ascii_letters+string.digits)*3+string.punctuation

password=[]

for i in range(n):
        new_char=random.choice(Char_list)
        password.append(new_char)
        
print("The random password is " + "".join(password))
