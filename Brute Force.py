import itertools
import time
import math


def distance(p1, p2):
    dist = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return dist


def question7():
    size = len(points)
    firstPoint = points[0]
    otherPoints = points[1:]
    permutations = list(itertools.permutations(otherPoints))

    optimalTourLength = distance(firstPoint, permutations[0][0])
    optimalOrder = str(hashmap.get(firstPoint))
    for x in range(size - 2):
        optimalTourLength = optimalTourLength + distance(permutations[0][x], permutations[0][x + 1])
        optimalOrder = optimalOrder + " -> " + str(hashmap.get(permutations[0][x]))
    optimalTourLength = optimalTourLength + distance(firstPoint, permutations[0][size - 2])
    optimalOrder = optimalOrder + " -> " + str(hashmap.get(permutations[0][size - 2]))
    optimalOrder = optimalOrder + " -> " + str(hashmap.get(firstPoint))

    permutations = permutations[1:]

    for permPoints in permutations:
        tourLength = distance(firstPoint, permPoints[0])
        order = str(hashmap.get(firstPoint))
        for x in range(size - 2):
            tourLength = tourLength + distance(permPoints[x], permPoints[x + 1])
            order = order + " -> " + str(hashmap.get(permPoints[x]))
        tourLength = tourLength + distance(firstPoint, permPoints[size - 2])
        order = order + " -> " + str(hashmap.get(permPoints[size - 2]))
        order = order + " -> " + str(hashmap.get(firstPoint))
        if tourLength < optimalTourLength:
            optimalTourLength = tourLength
            optimalOrder = order

    print(optimalOrder)
    print(optimalTourLength)


hashmap = dict()
points = []
num = 1
with open("Your file.txt") as file: # (1,2) file line example: 1,2
    for line in file:
        temp = line.strip().split(",")
        temp = tuple(list(map(int, temp)))
        points.append(temp)
        hashmap.update({temp: num})
        num = num + 1
file.close()

start_time = time.time()
question7()
print("Time elapsed: {:.2f}s".format(time.time() - start_time))
