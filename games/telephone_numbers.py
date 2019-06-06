n = 5 # 27
telephones = ["0412578440","0412199803","0468892011","112", "15"]

root = {}
count = 0
n = int(input())
for i in range(n):
    telephone = input()
    newDict = root
    for num in telephone:
        if num not in newDict:
            newDict[num] = {}
            count += 1
        newDict = newDict[num]
print(count)