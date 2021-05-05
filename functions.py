import random
points = 50
counter = 0
'''def printTheElements():
   response = input("Do you want to continue with the game? (Y/N)")
   if response.lower()=="yes" or response.lower()=="y":  return True
   else: return False'''
comparison = lambda arg,arg1: "is greater than {}.".format(arg1) if arg>arg1 else "is smaller than {}.".format(arg1)
evenOdd = lambda arg: "is odd." if arg & 1 == 1 else "is even."
divisible = lambda arg: check(arg,3,"divisible") if evenOdd(arg)=="is even." else check(arg,7,"divisible")
multiple = lambda arg: check(arg,10,"a multiple") if evenOdd(arg)=="is even." else check(arg,13,"a multiple") 

def factor(arg,arg1):
   lst = []
   for i in range(2,max(arg,arg1)+1):
      if arg%i==0 and arg1%i==0: lst.append(i)
   if len(lst)==0: return "doesn't have any common factor between the number and {}.".format(arg1)
   else: return "has {} common factors between the number and {} which are {}.".format(len(lst),arg1,lst)
 
def checkPrime(arg):
   for i in range(2,arg):
      if arg%i==0: 
        return "is a composite number."
        break
   else: return "is a prime number."
   
def check(arg,num,expr):
   if arg%num == 0: return "is {} by {}.".format(expr,num)
   else: return "is not {} by {}.".format(expr,num)
   
def takeRandom(arg):
   rand_num = random.randrange(1,101)
   if rand_num != arg: return rand_num
   return takeRandom(arg)

def guessTheNumber(arg):
   global points
   response = input("Guess the answer: ")
   if not response.isnumeric(): return -1
   else: 
      if int(response) == arg: 
         points += 50
         return True
      else: 
         points -= 10
         return False

def getPoint():
   return points
   
def getCounter():
   return counter
   
def statements():
   global counter
   counter += 1
   switch = {
      1: "first",
      2: "second",
      3: "third",
      4: "fourth",
      5: "fifth",
      6: "sixth"
   }
   return switch[counter]

def conditions(arg,arg1):
   global counter
   functions = {
      1: comparison(arg,arg1),
      2: evenOdd(arg),
      3: checkPrime(arg),
      4: divisible(arg),
      5: multiple(arg),
      6: factor(arg,arg1)
   }
   #if counter==7: return "You lost\nThe number is {}\nPoints: {}".format(arg,getPoints())
   return functions[counter]
   
def repeatTheGame():
    response = input("\nDo you want to continue or not?(y/n) ")
    if response.lower()[0] == 'y': return True
    else: return False

def setValues():
    global points, counter
    points = 50
    counter = 0