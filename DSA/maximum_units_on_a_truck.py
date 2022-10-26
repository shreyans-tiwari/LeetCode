"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

* numberOfBoxesi is the number of boxes of type i.
* numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""
boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
res = i = 0

boxTypes.sort(key=lambda x: x[1], reverse=True)

while truckSize > 0 and i < len(boxTypes):
    if truckSize - boxTypes[i][0] > 0:
        res += boxTypes[i][0] * boxTypes[i][1]
        truckSize -= boxTypes[i][0]
    else:
        res += truckSize * boxTypes[i][1]
        truckSize = 0

    i += 1

print(res)
