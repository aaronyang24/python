a,b =map(int,input("Enter the length and the width of the door: ").split())
c,d = map(int,input("Enter the length and width of the first wndow: ").split())
e,f = map(int,input("Enter the length and width of the second window: ").split())
g,h = map(int,input("Enter the length and width of the bookshelf: ").split())
i,j,k = map(int,input("Enter the length, width, and height of the room: ").split())
z = (((i*k)*2)+((j*k)*2)-(a*b)-(c*d)-(e*f)-(g*h))/120
print("\n"+"The amount of paint needed to paint the room: %3.2f" %z +" gallons" +".")