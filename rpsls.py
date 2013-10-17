import random
choices = ["rock", "spock", "paper", "lizard", "scissors"]

def name_to_number(name):
  if name in choices:
    return choices.index(name)
  else:
     return "invalid choice"


def number_to_name(number):
  if number < len(choices):
    return choices[number]
  else:
    return "invalid choice"  

def rpsls(name):
  user = name_to_number(name)
  computer = random.randrange(5)
  print "Player chooses ", name
  print "Computer chooses ", number_to_name(computer)
  mod = (user - computer) % 5
  if (mod >= 3):
    print "Computer wins!"
  elif (mod > 0):
    print "Player wins!"
  else:
    print "Player and Computer tie!"
  print "\n"
  

rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



