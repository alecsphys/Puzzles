import copy
import time


def main():
    puzzleQuestion(14)

    maxGridSize = 10
    timingList1 = []
    timingList2 = []

    for g in range(4, maxGridSize + 1):
        t0 = time.process_time()
        puzzle14solution1(g, printPaths=False)
        t1 = time.process_time()
        timingList1.append((t1-t0))
    print("Process time [sec] = ", timingList1, sum(timingList1))

    for g in range(4, maxGridSize + 1):
        t0 = time.process_time()
        puzzle14solution2(g, printPaths=False)
        t1 = time.process_time()
        timingList2.append((t1-t0))
    print("Process time [sec] = ", timingList2, sum(timingList2))


def puzzleQuestion(puzzleNumber):
    print("===========================================================================================================")
    print("Welcome to PTVuzzle - ", puzzleNumber)
    print("===========================================================================================================")
    print("You are on a grid of integers NxN in the position (0,0) and you have to go to the position (N,N).\n"
          "Only steps toward North and East  directions are allowed. How many different paths you can build that live\n"
          "totally above the diagonal connecting (0,0) with (N,N)? Can you design an efficient (in time and space)\n"
          "algorithm to fully enumerate all those paths?")
    print("===========================================================================================================")


def puzzle14solution1(gridSize, printPaths=True):
    print("Grid Size = ", gridSize)

    p = Path(gridSize)
    p.updateNorthCounter()
    p.updateSequence(1)
    pathList = [p]

    pathFinishedCounter = 0
    while len(pathList) > 0:
        pathNorth = copy.deepcopy(pathList.pop())
        pathEast = copy.deepcopy(pathNorth)
        if pathNorth.expandNorth() is not None:
            pathList.append(pathNorth)
        [pathEastFinished, pathEast] = pathEast.expandEast(printIfFinished=printPaths)
        if pathEastFinished:
            pathFinishedCounter += 1
        else:
            if pathEast is not None:
                pathList.append(pathEast)
    print("Total number of paths = ", pathFinishedCounter)


class Path:
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.sequence = []
        self.northCounter = 0

    def updateSequence(self, value):
        self.sequence.append(value)

    def updateNorthCounter(self):
        self.northCounter += 1

    def decodeSequence(self):
        stringfinal = ""
        for i in self.sequence:
            stringfinal += ("N" if i == 1 else "E")
        return stringfinal

    def expandNorth(self):
        newPath = None
        if self.northCounter < self.gridSize:
            self.updateNorthCounter()
            self.updateSequence(1)
            newPath = self
        return newPath

    def expandEast(self, printIfFinished=True):
        newPath = None
        pathFinished = False
        if len(self.sequence) < 2 * self.northCounter:
            self.updateSequence(0)
            newPath = self
        elif len(self.sequence) == 2 * self.gridSize:
            pathFinished = True
            if printIfFinished:
                print(self.decodeSequence())
        return [pathFinished, newPath]


def puzzle14solution2(gridSize, printPaths=True):
    print("Grid Size = ", gridSize)

    CT = createCatalanTriangle(gridSize)
    path = generatePath(CT, gridSize, index=1)
    if printPaths:
        print(path)
    for i in range(CT[gridSize-1][gridSize-1] - 1):
        generateNextPath(path)
        if printPaths:
            print(path)
    print("Total number of paths = ", CT[gridSize-1][gridSize-1])


def createCatalanTriangle(gridSize):
    CT = []
    row = [1]
    CT.append(row)
    for i in range(1, gridSize):
        row = [1]
        for j in range(1, i+1):
            if i == j:
                row.append(row[i-1] + CT[i-1][i-1])
            else:
                row.append(row[j-1] + CT[i-1][j])
        CT.append(row)
    return CT


def generatePath(catalanTriangle, gridSize, index):
    path = [0] * gridSize
    N = gridSize - 1
    p = 0
    s = 0
    path[p] = s
    p += 1
    while p <= N:
        while catalanTriangle[N-s][N-p] < index:
            index = index - catalanTriangle[N-s][N-p]
            s += 1
        path[p] = s
        p += 1
    return path


def generateNextPath(path):
    index = len(path) - 1
    while index > 0:
        if path[index] < index:
            path[index] += 1
            current = index + 1
            while current < len(path):
                path[current] = path[index]
                current += 1
            return True
        index -= 1
    return False


if __name__ == "__main__":
    main()
