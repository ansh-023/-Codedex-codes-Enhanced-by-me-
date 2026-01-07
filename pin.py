print("Bank of Codedex")
pin = int(input("Enter your pin :   "))
while pin != 1234 :
    pin =int(input("Incorrect PIN . enter your pin again :    "))
if pin == 1234:
    print(" Pin Accepted")