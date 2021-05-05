import functions
import random
#print(functions.greeting("Sanana"))
# Take two random numbers
random_1 = random_2 = 0
def takeRandomNumbers():
   global random_1, random_2
   random_1 = random.randrange(1,101)
   random_2 = functions.takeRandom(random_1)
   #print("Random1 = {} and Random2 = {}".format(random_1,random_2))

def repeatGuessing(arg,arg1,counter,flag):
    if flag is True:
      print("\nYour {} clue is: The number {}".format(functions.statements(),functions.conditions(arg,arg1))) if functions.getCounter()<6 else print("\nYou lost the game.\nThe number is {}\nPoints: {}".format(arg,functions.getPoint()))
    if counter!=7:
      response = functions.guessTheNumber(arg)
      print("Hurray! Correct answer\nPoints: {score}".format(score=functions.getPoint())) if response is True else print("Oops! Wrong answer\n Points: {score}".format(score=functions.getPoint())) if response is False else print("You haven't type the number correctly")
    else: response = True
    if response is False : repeatGuessing(arg,arg1,counter+1,flag=True)
    elif response == -1 : repeatGuessing(arg,arg1,counter+1,flag=False)
    elif  functions.repeatTheGame() is True: callback(True)
    

def callback(boolean):
    if boolean is True: functions.setValues()
    takeRandomNumbers()
    repeatGuessing(random_1,random_2,0,False)
    
callback(False)