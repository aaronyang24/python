from random import randint

def collectStringInput():
   print("Enter [R]ock, [P]aper, or [S]cissor")
   player = input("Player: ")
   return player.upper()

  
def generateIntegerValue():
   compChance = randint(1,100)
        
   if compChance < 33:
       computerChoice = 1 
   elif compChance >= 33 and compChance <= 66:
       computerChoice = 2 
   else:
       computerChoice = 3
   return computerChoice


def convertIntegerToRPS(intValue):
   """ Returns a string value: (P or p), (R or r), or (S or s) """
   if intValue == 1:
       print("\nComputer's selection: P")
       return 'P'
   elif intValue == 2:
       print("\nComputer's selection: R")
       return 'R'
   else:
       print("\nComputer's selection: S")
       return 'S'
      
      
def evaluateWinning(user, computer):
   """ returns a string value (announces the winner) """
   if (user=='R' and computer=='P') or (user=='P' and computer=='R'):
       if user == 'P':
           return "\nPaper covers Rock.\nUser WINS! "
       else:
           return "\nPaper covers Rock.\nComputer WINS! "

   elif (user=='R' and computer=='S') or (user=='S' and computer=='R'):
       if user == 'R':
           return "\nRock smashes scissors.\nUser WINS! "
       else:
           return "\nRock smashes scissors.\nComputer WINS! "
  
   elif (user=='P' and computer=='S') or (user=='S' and computer=='P'):
       if user == 'S':
           return "\nScissors cut paper.\nUser WINS! "
       else:
           return "\nScissors cut paper.\nComputer WINS! " 
                  
   else:
       return "\nTie!"
  
  
def main():
   user = collectStringInput()
   cIntVal = generateIntegerValue()
   computer = convertIntegerToRPS(cIntVal)
   print(evaluateWinning(user, computer))
  
main()