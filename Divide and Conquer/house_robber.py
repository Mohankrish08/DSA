def HouseRobber(house, index):
    if index >= len(house):
        return 0
    else:
        first = house[index] + HouseRobber(house, index+2)
        skip = HouseRobber(house, index+1)
    return max(first, skip)


house = [6,7,1,30,8,2,4]

print(HouseRobber(house, 0))