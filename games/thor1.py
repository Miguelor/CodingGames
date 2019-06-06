lx, ly, tx, ty = [int(i) for i in input().split()]

x = tx - lx
y = ty - ly
    
while True:
    #remaining_turns = int(input())
    xa, ya = "", ""
    if x < 0:
        xa = "E"
        x += 1
    elif x > 0:
        xa = "W"
        x -= 1
    if y > 0:
        ya = "N"
        y -= 1
    elif y < 0:
        ya = "S"
        y += 1
    
    print(ya + xa)    
        
    if (x == 0) & (y == 0):
        break