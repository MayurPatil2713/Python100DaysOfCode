#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

# s w g
# 0 1 2
c = input("Computer: ")
p = input("Player: ")
if(c == p):
    print("match draw")
elif(c == "s" and p == "w"):
    print("Snakes beats water, Lose")
elif(c == "s" and p == "g"):
    print("Gun beat snake, Win")
elif(c == "w" and p == "s"):
    print("Win")
elif(c == "w" and p == "g"):
    print("Lose")
elif(c == "g" and p == "s"):
    print("Lose")
elif(c == "g" and p == "w"):
    print("Win")
else:
    print("Enter valid input")

