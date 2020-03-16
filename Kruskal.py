import time
import math
import matplotlib.pyplot as plt


def setNodeDictsList(nodeorderdict, connectnodesdict, nodelist):
    with open("points16.txt") as file:
        order = 0
        for line in file:
            order = order + 1
            temp = line.strip().split(",")
            temp = tuple(list(map(float, temp)))
            nodelist.append(temp)
            nodeorderdict.update({temp: order})
            connectnodesdict.update({temp: 0})
    file.close()


def plotEdge(edgetuple):
    x = []
    y = []
    x.append(edgetuple[0][0])
    x.append(edgetuple[1][0])
    y.append(edgetuple[0][1])
    y.append(edgetuple[1][1])
    plt.plot(x, y)


def distanceBetweenNodes(node1, node2):
    distance = math.sqrt((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1]) ** 2)
    return distance


def getEdges(nodelist):
    edgeList = []
    numOfNodes = len(nodelist)
    noDuplicate = 1
    for i in range(numOfNodes):
        for j in range(numOfNodes - i - 1):
            trio = (nodes[i], nodes[j + noDuplicate], distanceBetweenNodes(nodes[i], nodes[j + noDuplicate]))
            edgeList.append(trio)
        noDuplicate += 1
    return sorted(edgeList, key=lambda x: (x[2], x[0][0], x[1][0], x[0][1], x[1][1]))


def minimumSpanningTree(edgelist, connectednodedict, nodeorderdict):
    requiredNumOfEdges = len(nodes) - 1
    usedEdges = []
    tourLength = 0
    while sum(x == 0 for x in connectednodedict.values()) > 0:
        tempPoint = edgelist.pop(0)
        if connectednodedict[tempPoint[0]] < 1 or connectednodedict[tempPoint[1]] < 1:
            connectednodedict[tempPoint[0]] += 1
            connectednodedict[tempPoint[1]] += 1
            usedEdges.append(tempPoint)
            tourLength += tempPoint[2]
    i = 0
    while i < len(usedEdges):
        if requiredNumOfEdges == len(usedEdges):
            break
        if connectednodedict[usedEdges[i][0]] > 1 and connectednodedict[usedEdges[i][1]] > 1:
            connectednodedict[usedEdges[i][0]] -= 1
            connectednodedict[usedEdges[i][1]] -= 1
            usedEdges.remove(usedEdges[i])
            i -= 1
        i += 1
    for edge in usedEdges:
        plotEdge(edge)
    plt.show()
    #for edge in usedEdges:
        #print(nodeorderdict.get(edge[0]), "->", nodeorderdict.get(edge[1]))
    print("Tree length:", tourLength)


def travellingSalesMan(edgelist, connectednodedict, nodeorderdict):
    requiredNumOfEdges = len(nodes)
    usedEdges = []
    tourLength = 0
    while edgelist and len(usedEdges) < requiredNumOfEdges:
        tempPoint = edgelist.pop(0)
        if connectednodedict[tempPoint[0]] < 2 and connectednodedict[tempPoint[1]] < 2:
            connectednodedict[tempPoint[0]] += 1
            connectednodedict[tempPoint[1]] += 1
            usedEdges.append(tempPoint)
            tourLength += tempPoint[2]
            if 2 < len(usedEdges) < requiredNumOfEdges and sum(x == 1 for x in connectednodedict.values()) == 0:
                usedEdges.pop()
                connectednodedict[tempPoint[0]] -= 1
                connectednodedict[tempPoint[1]] -= 1
                tourLength -= tempPoint[2]
    for edge in usedEdges:
        plotEdge(edge)
    plt.show()
    #for edge in usedEdges:
        #print(nodeorderdict.get(edge[0]), "->", nodeorderdict.get(edge[1]))
    print("Tour length:", tourLength)


nodeOrders = dict()
connectedNodes = dict()
nodes = []
setNodeDictsList(nodeOrders, connectedNodes, nodes)

print("Kruskal Implementation")
startTime = time.time()

edges = getEdges(nodes)
#minimumSpanningTree(edges, connectedNodes, nodeOrders)
travellingSalesMan(edges, connectedNodes, nodeOrders)

print("Time elapsed: {:.2f}s".format(time.time() - startTime))
