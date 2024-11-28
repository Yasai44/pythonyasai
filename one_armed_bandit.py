print( "WELCOME TO CONESTOGA CASINO")
input("Press Enter to play")

reel1 = random.randint(1 , 3)
reel2 = random.randint(1 , 3)
reel3 = random.randint(1 , 3)

#print(reel1, reel2, reel3)

#Use match to determine what symbol to show
match reel1:
    case 1:
        print("$", end=" ")
    case 2:
        print("@", end=" ")
    case 3:
        print("%", end=" ")

match reel2:
    case 1:
        print("$", end=" ")
    case 2:
        print("@", end=" ")
    case 3:
        print("%", end=" ")

match reel3:
    case 1:
        print("$")
    case 2:
        print("@")
    case 3:
        print("%")

#Determine results
if reel1 == reel2 and reel2 == reel3:
    print("YOU WIN!!!!!!")
elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
    print("AWWWW SO CLOSE")
else:
    print("YOU LOSE")
print("heuuuuuuuuuuuuuuuuu")