gp = rp = hp = sp = 0

q1 = int(input("Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
q2 = int(input("When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
q3 = int(input("Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if q1 == 1:
    gp += 1
    rp += 1
elif q1 == 2:
    hp += 1
    sp += 1
else:
    print("Invalid choice for Q1")
if q2 == 1:
    hp += 2
elif q2 == 2:
    sp += 2
elif q2 == 3:
    rp += 2
elif q2 == 4:
    gp += 2
else:
    print("Invalid choice for Q2")
if q3 == 1:
    hp += 4
elif q3 == 2:
    sp += 4
elif q3 == 3:
    rp += 4
elif q3 == 4:
    gp += 4
else:
    print("Invalid choice for Q3")
print(f"Total points of Gryffindor: {gp}")
print(f"Total points of Ravenclaw: {rp}")
print(f"Total points of Hufflepuff: {hp}")
print(f"Total points of Slytherin: {sp}")
