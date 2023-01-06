import random

name = "Pele"
question = "Am I the best soccer player of the world?"
answer = ""

if question == "":
  print("Error! You must provide a valid YES or NO question for it to work!")
else:
  random_number = random.randint(1,10)
  #print("random: {0}".format(random_number))

  # logic follows
  if (random_number == 1):
    answer = "Yes - definitely."
  elif (random_number == 2):
    answer = "It is decidedly so."
  elif (random_number == 3):
    answer = "Without a doubt."
  elif (random_number == 4):
    answer = "Reply hazy, try again."
  elif (random_number == 5):
    answer = "Ask again later."
  elif (random_number == 6):
    answer = "Better not tell you now."
  elif (random_number == 7):
    answer = "My sources say no."
  elif (random_number == 8):
    answer = "Outlook not so good."
  elif (random_number == 9):
    answer = "Very doubtful."
  elif (random_number == 10):
    answer = "Don't count on it."
  else:
    answer = "Error"

  if name != "":
    print("[{0}] asks: [{1}]".format(name, question))
  else:
    print("Question: [{0}]".format(question))

  print("Magic 8-Ball's answer: {0}".format(answer))
