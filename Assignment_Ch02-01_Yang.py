time = int(input("Enter the elapsed time in seconds: "))
hours = time // 3600
remainder = time % 3600
min = remainder // 60
sec = remainder % 60
print("\n" + "The elapsed time in seconds = " + str(time ))
print ("\n" + "The equivalent time in hours:minutes:seconds = " + str(hours) +":" + str(min)+":" + str(sec) )