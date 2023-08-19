from collections import deque
graph = {
    '0': ['4','7'],
  '1': [],
  '2': [],
  '3': ['6'],
  '4': ['0'],
  '6': ['3'],
  '7': ['0'],
  '8': []
}

def getConnectedComponents(graph, startingNode, visitedNodes):
    if startingNode in visitedNodes:
        return 0
    
    visitedNodes.add(startingNode)
    result = 1

    for neighbour in graph[startingNode]:
        result += getConnectedComponents(graph, neighbour, visitedNodes)
    
    return result

def getLargestComponent(graph):

    visitedNodes = set()
    maximumConnectedComponent = 0

    for node in graph.keys():
        connectedComponents = getConnectedComponents(graph, node, visitedNodes)
        # print(node, connectedComponents)
        maximumConnectedComponent = max(maximumConnectedComponent, connectedComponents)

    return maximumConnectedComponent

# print(getLargestComponent(graph))




def getAdjacencyListFromEdges(edges):

    adjacencyList = {}
    for edge in edges:
        if edge[0] not in adjacencyList:
            adjacencyList[edge[0]] = []
        if edge[1] not in adjacencyList:
            adjacencyList[edge[1]] = []

        adjacencyList[edge[0]].append(edge[1])
        adjacencyList[edge[1]].append(edge[0])

    return adjacencyList


def shortestPath(edges, source, destination):

    graph = getAdjacencyListFromEdges(edges)
    
    queue = deque()
    queue.append((source, 0))

    visitedSet = set()

    while queue:
        
        currentNode, numberOfEdges = queue.popleft()
        if currentNode in visitedSet:
            continue

        visitedSet.add(currentNode)
        if currentNode == destination:
            return numberOfEdges
        
        numberOfEdges += 1
        for neighbour in graph[currentNode]:
            queue.append((neighbour, numberOfEdges))

    return -1

edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

# print(shortestPath(edges, 'm', 's'))

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]


def islandCountUtil(grid, row, col, visited):

    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 'W' or (row,col) in visited:
        return 0
    
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited.add((row,col))
    # print(row,col)

    connectedComponentCount = 1
    for (rowOffset, colOffset) in offsets:
        connectedComponentCount += islandCountUtil(grid, row+rowOffset, col+colOffset, visited)
        # print(connectedComponentCount)
    
    return connectedComponentCount

def islandCount(grid):

    currentCount = 1000
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            
            if grid[row][col] == "L" and (row, col) not in visited:
                # print("SS")
                currentCount = min(currentCount, islandCountUtil(grid, row, col, visited))
    

    return currentCount

print(islandCount(grid))
            
