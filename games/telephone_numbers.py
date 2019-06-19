# Example
# 5 
# 0412578440 
# 0412199803 
# 0468892011 
# 112 
# 15

# create empty dictionary and counter
root = {}
count = 0
# input size
n = int(input())
for i in range(n):
    # input telephone
    telephone = input()
    # create tree like structure with dictionaries
    # adding a new dictionary into the last level dict
    # if the value is not found
    # every time that new dictionary is added add 1 to the counter
    newDict = root
    for num in telephone:
        if num not in newDict:
            newDict[num] = {}
            count += 1
        newDict = newDict[num]
print(count)
