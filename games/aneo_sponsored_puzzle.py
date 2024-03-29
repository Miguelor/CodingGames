# Input
speed, lights = int(input()), int(input())

# Input distance and duration
# for each traffic light, check all speeds, from 1 to the limit, 
# if the car can pass through that light without stopping
for i in range(lights):
    distance, duration = [int(j) for j in input().split()]
    globals()[ "possible_speed_" + str(i)] = list()
    for s in range(speed, 0, -1):  
        period = (distance / (s/3.6))/duration
        if (round(period)-period) < 0.000005:
            period = round(period)
        if int(str((period) % 2)[0]) == 0:
            globals()[ "possible_speed_" + str(i)].append(s)

# find the maximun speed contained in all the "possible_speed"
solutions_speed = list()
for i in range(lights):
    if i == 0:
        solutions_speed = globals()[ "possible_speed_" + str(i)]
    else:
        solutions_speed = [i for i in globals()[ "possible_speed_" + 
                           str(i)] if i in solutions_speed]

print(str(max(solutions_speed)))
