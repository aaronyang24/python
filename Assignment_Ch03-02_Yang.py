p1 = input("Enter [R]ock, [P]aper, or [S]cissor\nPlayer 1: ")
p2 = input("Enter [R]ock, [P]aper, or [S]cissor\nPlayer 2: ")

if p1 == p2 :
    print("Nobody WINS!")
elif p1 == "R" or p1 == "r" :
    if p2 == "P" or p2 =="p" :
        print("\nPaper beats rock.\nPlayer 2 WINS!")
    else: 
        print("\nRock beats scissor.\nPlayer 1 WINS! ")
elif p1 == "P" or p1 == "p":
    if p2 == "S" or p2 == "s":
        print("\nScissor cuts paper.\nPlayer 2 WINS!")
    else:
        print("\Paper beats rock.\nPlayer 1 WINS!")
elif p1 == "S" or p1 == "s" :
    if p2 == "R" or p2 == "r" :
        print("\nRock beats scissor.\nPlayer 2 WINS!")
    else:
        print("\nScissor beats paper.\nPlayer 1 WINS!")
else:
    print("Enter Rock, Paper, or Scissors")        