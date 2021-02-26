class node:
    def __init__(self, identifier):
        self.distanceVector = dict()
        self.distanceVector["a"] = 9999
        self.distanceVector["b"] = 9999
        self.distanceVector["c"] = 9999
        self.distanceVector["d"] = 9999
        self.distanceVector["e"] = 9999
        self.distanceVector["f"] = 9999
        self.distanceVector["g"] = 9999
        self.distanceVector["h"] = 9999
        self.distanceVector[identifier] = 0
        
        self.name = identifier
        self.neighbors = dict()
    
    def addNeighbor(self, neighbor, distance):
        self.distanceVector[neighbor] = distance
        self.neighbors[neighbor] = ""

    def initNeighborVector(self, neighbor, neighborVector):
        self.neighbors[neighbor] = neighborVector

    def updateVector(self, neighborVector):
       for neighbor in self.neighbors:



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

 
