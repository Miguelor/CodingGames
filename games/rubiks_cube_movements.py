# Example
# Input
# face_1 = "L"
# face_2 = "B"
# rotationsVector = ['x', 'y', "x'", 'z', y]
# Output
# B
# L

rotations = input()
face_1 = input()
face_2 = input()

rotationsVector = rotations.split()

dice = ['F', 'B', 'U', 'D', 'L', 'R']
possibleRotations = {"x":(3,2,0,1,4,5),
                     "x'":(2,3,1,0,4,5),
                     "y":(5,4,2,3,0,1),
                     "y'":(4,5,2,3,1,0),
                     "z":(0,1,4,5,3,2),
                     "z'":(0,1,5,4,2,3)}

newDice = dice
for rotation in rotationsVector:
    print(rotation)
    newDice = list(newDice[x] for x in possibleRotations[rotation])

print(dice[newDice.index(face_1)])
print(dice[newDice.index(face_2)])
