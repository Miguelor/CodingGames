# Example
# Input
#57
#70545
#31 PLAIN 30
#18 PLAIN 35
#14 PLAIN 32
#25 ODD
#13 PLAIN 9
#14 PLAIN 34
#32 ODD
#26 PLAIN 9
#29 EVEN
#7 PLAIN 21
#32 PLAIN 29
#0 PLAIN 7
#7 PLAIN 34
#13 PLAIN 14
#22 PLAIN 8
#25 PLAIN 28
#11 PLAIN 20
#14 ODD
#23 ODD
#13 PLAIN 22
#2 ODD
#23 EVEN
#17 ODD
#30 EVEN
#28 PLAIN 28
#5 PLAIN 36
#13 EVEN
#22 PLAIN 11
#5 EVEN
#32 PLAIN 25
#13 ODD
#10 EVEN
#28 ODD
#15 PLAIN 2
#33 EVEN
#29 ODD
#1 EVEN
#19 PLAIN 12
#0 PLAIN 34
#24 EVEN
#16 PLAIN 36
#4 EVEN
#35 PLAIN 13
#14 PLAIN 34
#30 ODD
#13 EVEN
#29 ODD
#7 EVEN
#18 PLAIN 20
#33 ODD
#24 PLAIN 28
#34 PLAIN 34
#33 EVEN
#32 EVEN
#10 EVEN
#13 ODD
#35 PLAIN 26
# 
# Output
# 1153

import math

# Input rounds and cash
rounds, cash = int(input()), int(input())

# loop over rounds
for i in range(rounds):
    
    # Split play elements
    play = input().split(" ")
    # Bet 1/4 of current money
    bet = math.ceil(cash/4)
    # first element is the result
    result = int(play[0])
    # and what he calls for 
    call = play[1]
    
    # check if he calls for the result,
    # losing the bet if false
    # and multiplying for 35 if true
    if (call == 'PLAIN'):
        if result == int(play[2]):
            cash = cash + bet*35
        elif result != int(play[2]):
            cash = cash - bet
            
    # check if result is even and non-zero
    elif (int(str(result % 2)[0]) == 0) & (result != 0) & (call == 'EVEN'): 
        cash = cash + bet
    
    # check if result is even
    elif (int(str(result % 2)[0]) != 0) & (call == 'ODD'):
        cash = cash + bet
    
    # if he doesn't call for PLAIN and lose
    else:
        cash = cash - bet

# print final cash
print(cash)