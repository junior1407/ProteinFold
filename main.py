

bestForms = []
bestEnergy = 99999


def toString(taken):
    pass
    maxX=0
    maxY=0
    minY=0
    minX=0
    string = ""

    for key in taken:
        x,y = key
        if (x>maxX):
            maxX = x
        if (x<minX):
            minX=x
        if(y<minY):
            minY=y
        if (y>maxY):
            maxY=y
    for i in range(minX,maxX+1):
        for j in range(minY,maxY+1):
            if ((i,j) in taken):
                string= string + taken[(i,j)]
            else:
                string= string + '*'
        string+='\n'

    return string

class Node():
    def __init__(self, previous, pos, index):
        x,y= pos
        global sequence, bestForms, bestEnergy
        #Se já tiver acabado.
        if index == len(sequence):
            energy = previous.evaluate()
            if energy< bestEnergy:
                bestForms = []
                bestForms.append(toString(previous.taken))
                bestEnergy = energy
            elif energy == bestEnergy:
                bestForms.append(toString(previous.taken))
            return None
        #Se a posicao estiver ocupada
        #Caso inicial
        if (previous is None):
            self.previous = None
            self.taken = {}
        else:
            if pos in previous.taken:
                return None
            self.previous = previous
            self.taken = previous.taken.copy()
        self.taken[pos] = sequence[index]
        self.value = sequence[index]
        self.position = pos
        self.posibilities = []
        self.posibilities.append(Node(self,(x+1,y), index+1))
        self.posibilities.append(Node(self, (x-1, y), index + 1))
        self.posibilities.append(Node(self,(x,y+1), index+1))
        self.posibilities.append(Node(self, (x, y-1), index + 1))

    def evaluate(self):
        verified = {}
        curr = self
        while(curr is not None):
            if (curr.value == 'H'):
                x,y = curr.position
                if (x+1,y) in self.taken:
                    if self.taken[(x+1,y)] == 'H':
                        if (curr.position, (x+1,y)) not in verified:
                            verified[curr.position, (x+1,y)] = 1
                            verified[ (x + 1, y), curr.position] = 1
                if (x-1,y) in self.taken:
                    if self.taken[(x-1,y)] == 'H':
                        if (curr.position, (x-1,y)) not in verified:
                            verified[curr.position, (x-1,y)] = 1
                            verified[ (x - 1, y), curr.position] = 1
                if (x,y+1) in self.taken:
                    if self.taken[(x,y+1)] == 'H':
                        if (curr.position, (x,y+1)) not in verified:
                            verified[curr.position, (x,y+1)] = 1
                            verified[ (x, y+1), curr.position] = 1
                if (x,y-1) in self.taken:
                    if self.taken[(x,y-1)] == 'H':
                        if (curr.position, (x,y-1)) not in verified:
                            verified[curr.position, (x,y-1)] = 1
                            verified[ (x, y-1), curr.position] = 1
            curr = curr.previous

        return -1 * (len(verified)/2)





file =open("input2.txt", "r")
sequence = file.readline()
pos = 0
start = Node(None,(0,0), 0)
print(bestEnergy)
bestForms = list(set(bestForms))
print(bestForms)
for candidate in bestForms:
    print(candidate)
    pass
    #candidate.prinT()
    #print()
