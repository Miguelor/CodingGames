#3
#1 2 3
#9
#
#4
#1 4 3 4
#24
#
#9
#9 9 9 9 9 9 9 9 9
#261

n = int(input())
nums = [ int(x) for x in input().split(" ") ]

cost = 0
while len(nums) > 1 :
    nums.sort()
    low = nums[:2]
    del nums[:2]
    cost += sum(low)
    nums.append(sum(low))
