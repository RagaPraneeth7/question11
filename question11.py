t = int(input())                # read number of test cases

for i in range(t):              # for each element from range 0 and t
    n = input()                 # read string input 
    if(n.upper() == 'B' ):      # if n equals to B, print Battleship
        print("BattleShip")
    elif(n.upper() == 'C'):     # else if n equals to C, print Cruiser
        print("Cruiser")
    elif(n.upper() == 'D'):     # else if n equals to D, print Destroyer
        print("Destroyer")
    elif(n.upper() == 'F'):     # else if n equals to F, print Frigate
        print("Frigate")