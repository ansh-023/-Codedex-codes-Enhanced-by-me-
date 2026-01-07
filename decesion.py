import random
ques= input("Eneter your Question :      ")
num = random.randint(1,9)
if num == 1:
  a=("Yes - definitely.")
elif num == 2:
  a=("It is decidedly so.")
elif num == 3:
  a=("Without a doubt.")
elif num == 4:
  a=("Reply hazy, try again")
elif num ==5:
  a=("Ask again later")
elif num == 6:
  a=("Better not tell you now.")
elif num == 7:
  a=("My sources say no.")
elif num == 8:
  a=("Outlook not so good")
elif num == 9:
  a=("Very doubtful")
print(f"answer :{a}")