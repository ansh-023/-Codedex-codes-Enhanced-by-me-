import random
num= random.randint(1,10)
print(num)
a= 5 #max tries
tries= 0 
d = int(input(" Enter you guess :   "))# guessed by the user
while d != num:
    tries += 1 
    r = a - tries
    if r >0:
        print(f"incorrect {r} tries remaing ")
        d = int(input(" Its incorrect try again :   "))
    else:
        break 
    print("You are good at nothing ")
if d == num and tries <= 5 :
    print("Yes its correct ")