a,b,c = input ("Please input three integers:\n").split()
if a < b < c :
    pass
elif a > c :
    a , c = c , a
elif a > b :
    a , b = b, a
elif b > c :
    b , c = c , b 

print ( "\nThree integer number in ascending order:\n"+a+" "+b+" "+c) 