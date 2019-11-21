flag=True
while(flag):
    print("Enter two positive integer numbers.")
    print("First number must be less than the second number:")
    print("Enter numbers:",end=' ')
    try:#using try
        firstNum,secondNum=input().split() #taking input numbers
        firstNum=int(firstNum) #coverting firstNum to int
        secondNum=int(secondNum) #coverting secondNum to int
        if(firstNum>secondNum): #checking number
            print("First number must be less than the second number!Please try again.")
        elif(firstNum < 0):
            print("No negative numbers!Please try again.")
        else:
            print("Odd integers between",str(firstNum),"and",str(secondNum),"are:")
            for i in range(firstNum,secondNum+1,1):
                if(i%2!=0): #checking odd numbers
                    print(i,end=' ') #print odd number
            print() #used for newline
            #for loop is used for sum of even numbers
            sum=0 #declaring variable to store sum
            for i in range(firstNum,secondNum,1):
                if(i%2==0): #checking even numbers
                    sum=sum+i #sum of even numbers
            print("Sum of even integers between",str(firstNum),"and",str(secondNum),"=",str(sum))
            #for loop is used for sum of square of odd numbers
            sumSquares=0 #variable to store sum of odd squares
            for i in range(firstNum,secondNum+1,1):
                if(i%2!=0):#checking odd number
                    sumSquares+=i*i #square odd number and add to sum
            print("Sum of the squares of odd integers between",str(firstNum),"and",str(secondNum),"=",str(sumSquares))
            choice=input("Do you want to repeat this program? y/n ")#asking user
            if(choice=="y"):
                continue #continue while loop
            elif(choice=="n"):
                flag=False #set flag to false to break the loop
                print("Bye!") #display message
            else:
                print("Enter valid choice") #display for invalid choice
    except ValueError:
        print("Incorrect Input.Please try again.") #display error message