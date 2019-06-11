# Example
# 50
# 3
# RSLJ97 134 1447409503
# RSLJ97 185 1447413099
# RSLJ97 201 1447420298

# Input 
l = int(input())
n = int(input())
pics = list()
cars = list()
# get uniques cars list
for i in range(n) :
    pics.append(input().split(" "))
    if pics[i][0] not in cars :
        cars.append(pics[i][0])

# loop for each car
# get all pics of that car
# check if he exceded de limit
# between two points
exc = False
for i in range(len(cars)) :
    car = [k for k in pics if cars[i] in k]
    for c in range(1, len(car)) :
        dist = int(car[c][1]) - int(car[c-1][1]) 
        time = (int(car[c][2]) - int(car[c-1][2]))/3600
        if dist/time > l :
            print(" ".join(car[c][:2]))
            exc = True
            
if exc != True :
    print("OK")
    
