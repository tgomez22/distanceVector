class node:
    def __init__(self, identifier):
        self.distanceVector = dict()
        self.distanceVector[identifier] = 0
        self.name = identifier
        self.hasChanged = False
    
    def addNeighbor(self, neighbor, distance):
        self.distanceVector[neighbor] = distance

    def updateVector(self, neighbor, neighborVector):
        for node in neighborVector.keys():
            if node in self.distanceVector.keys():
                originalValue = self.distanceVector[node]
                self.distanceVector[node] = min(self.distanceVector[node], self.distanceVector[neighbor] + neighborVector[node] )
                if(originalValue != self.distanceVector[node]):
                    self.hasChanged = True
                    return
                else:
                    self.hasChanged = False
            else:
                self.distanceVector[node] = self.distanceVector[neighbor] + neighborVector[node]
                self.hasChanged = True
                return

    def displayVectorTable(self, iteration):
        print(f"For iteration {iteration}: \n")
        for nodes in self.distanceVector.keys():
            print(f"Node: {nodes} - distance: {self.distanceVector[nodes]}\n")


a = node("a")
a.addNeighbor("b", 14)
a.addNeighbor("c", 2)

b = node("b")
b.addNeighbor("a", 14)
b.addNeighbor("c", 8)
b.addNeighbor("f", 3)
b.addNeighbor("e", 1)

c = node("c")
c.addNeighbor("a", 2)
c.addNeighbor("b", 8)
c.addNeighbor("g", 1)

d = node("d")
d.addNeighbor("e", 7)
d.addNeighbor("f", 10)

e = node("e")
e.addNeighbor("d", 7)
e.addNeighbor("f", 1)
e.addNeighbor("b", 1)

f = node("f")
f.addNeighbor("b", 3)
f.addNeighbor("g", 3)
f.addNeighbor("h", 1)
f.addNeighbor("e", 1)
f.addNeighbor("d", 10)

g = node("g")
g.addNeighbor("c", 1)
g.addNeighbor("f", 3)
g.addNeighbor("h", 5)

h = node("h")
h.addNeighbor("g", 5)
h.addNeighbor("f", 1)

iteration = 0
a.displayVectorTable(iteration)

a.updateVector("b", b.distanceVector)
a.updateVector("c", c.distanceVector)

iteration += 1
a.displayVectorTable(iteration)

while(a.hasChanged == True):
    b.updateVector("a", a.distanceVector)
    b.updateVector("c", c.distanceVector)
    b.updateVector("e", e.distanceVector)
    b.updateVector("f", f.distanceVector)

    c.updateVector("a", a.distanceVector)
    c.updateVector("b", b.distanceVector)
    c.updateVector("g", g.distanceVector)

    d.updateVector("e", e.distanceVector)
    d.updateVector("f", f.distanceVector)

    e.updateVector("d", d.distanceVector)
    e.updateVector("b", b.distanceVector)
    e.updateVector("f", f.distanceVector)

    f.updateVector("b", b.distanceVector)
    f.updateVector("e", e.distanceVector)
    f.updateVector("g", g.distanceVector)
    f.updateVector("h", h.distanceVector)

    g.updateVector("c", c.distanceVector)
    g.updateVector("f", f.distanceVector)
    g.updateVector("h", h.distanceVector)

    h.updateVector("f", f.distanceVector)
    h.updateVector("g", g.distanceVector)

    iteration += 1
    a.updateVector("b", b.distanceVector)
    a.updateVector("c", c.distanceVector)
    a.displayVectorTable(iteration)
