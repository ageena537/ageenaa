'''''
print("Rules:\nChoose the number of sticks(1,2 or 3)\nThe person to pick the last stick loses")
print("The available no.of sticks:16")
name1=input("enter the name of first player")
name2=input("enter the name of second player")
def stickman():
    no_of_sticks=16
    inp=int(input(name1,"pick no of sticks(1/2/3):"))
    sam=int(input(name2,"pick no.of sticks:"))
    while True:
       remains=no_of_sticks-inp
       if inp in [1,2,3]:
           print(remains,"sticks are available now")
       else:
           print("incorrect no of sticks")

       if no_of_sticks==remains:
           print("you lose")
           break
       else:
           print("hah")
stickman()
'''''
print('Set contains 1, 2, or 3 sticks.\nThe player who takes the last stick is the loser.')
person1=input("enter the name:")
person2=input("enter the name:")
stick=16
while stick!=0:
    if stick!=0:
        print("the sticks remaining is:",stick)
        choice=int(input(f"{person1},The no: of sticks player can take 1,2 or 3:"))
        stick=stick-choice
        player=person1
    if stick!=0:
        print(stick)
        choice=int(input(f"{person2},The no: of sticks player can take 1,2 or 3:"))
        stick=stick-choice
        player=person2
    if stick==0:
         print(f"{player}, is the loser.")

