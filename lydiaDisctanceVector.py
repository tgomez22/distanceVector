import math


class node:
    def __init__(self,neighbors:list):

        self.table = {
                "a" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            },
                "b" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            },
                "c" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            },
                "d" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            },
                "e" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            },
                "f" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            },
                "g" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            },
                "h" : {
                                "a":math.inf,
                                "b":math.inf,
                                "c":math.inf,
                                "d":math.inf,
                                "e":math.inf,
                                "f":math.inf,
                                "g":math.inf,
                                "h":math.inf
                            }
            }
        self.neighbors = neighbors

    def cost(self, sourceNode,destNode):
        return self.table[sourceNode][destNode]

    def updateCost(self, sourceNode, destNode, distance):
        self.table[sourceNode][destNode]=distance

    # def updateTable(self, neighborNode):
    #     for src in self.table.keys():
    #         for dest in src.keys():
    #             if neighborNode[src] self.cost(src,dest)





a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"
class network:

    def __init__(self):
        self.nodes = {
            a:node([b,c]),
            b:node([a,c,e,f]),
            c:node([a,b,g]),
            d:node([e,f]),
            e:node([b,d,f]),
            f:node([b,d,e,g,h]),
            g:node([c,f,h]),
            h:node([f,g])
        }


    def sendVectorToNeighbors(self, sourceNode):
        for neighbor in self.nodes[sourceNode].neighbors:
           for src in self.nodes[sourceNode].table.keys():
               for dest in self.nodes[sourceNode].table[src]:
                    distancefromSrcToDestThroughNeighbor = self.nodes[sourceNode].cost(src,neighbor) + self.nodes[neighbor].cost(neighbor,dest)
                    if distancefromSrcToDestThroughNeighbor < self.nodes[sourceNode].cost(src,dest):
                        self.nodes[sourceNode].updateCost(src,dest,distancefromSrcToDestThroughNeighbor)
                    # else: value in sourceNode table smaller than gonig to dest through neighbor

    def print(self):
        for node in self.nodes.keys():
            print(f"node:{node}")
            for row in self.nodes[node].table.keys():
                print(f"row: {row} {self.nodes[node].table[row]}")
            print()

    def printNode(self,node):
        print(f"node: {node}")
        table = self.nodes[node].table
        for row in table.keys():
            print(f"row {row}: {table[row]}")

mynetwork = network()
 #initialize A
mynetwork.nodes[a].updateCost(a,a,0)
mynetwork.nodes[a].updateCost(a,b,14)
mynetwork.nodes[a].updateCost(a,c,2)

#initialize B
mynetwork.nodes[b].updateCost(b,a,14)
mynetwork.nodes[b].updateCost(b,b,0)
mynetwork.nodes[b].updateCost(b,c,8)
mynetwork.nodes[b].updateCost(b,e,10)
mynetwork.nodes[b].updateCost(b,f,3)

#initialize C
mynetwork.nodes[c].updateCost(c,a,2)
mynetwork.nodes[c].updateCost(c,b,8)
mynetwork.nodes[c].updateCost(c,c,0)
mynetwork.nodes[c].updateCost(c,g,1)

#initialize D
mynetwork.nodes[d].updateCost(d,d,0)
mynetwork.nodes[d].updateCost(d,e,7)
mynetwork.nodes[d].updateCost(d,f,10)

#initialize E
mynetwork.nodes[e].updateCost(e,b,1)
mynetwork.nodes[e].updateCost(e,d,7)
mynetwork.nodes[e].updateCost(e,e,0)
mynetwork.nodes[e].updateCost(e,f,1)

#initialize F
mynetwork.nodes[f].updateCost(f,b,3)
mynetwork.nodes[f].updateCost(f,d,10)
mynetwork.nodes[f].updateCost(f,e,1)
mynetwork.nodes[f].updateCost(f,f,0)
mynetwork.nodes[f].updateCost(f,g,3)
mynetwork.nodes[f].updateCost(f,h,1)

#initialize G
mynetwork.nodes[g].updateCost(g,c,1)
mynetwork.nodes[g].updateCost(g,f,3)
mynetwork.nodes[g].updateCost(g,g,0)
mynetwork.nodes[g].updateCost(g,h,5)

#initialize H
mynetwork.nodes[h].updateCost(h,f,1)
mynetwork.nodes[h].updateCost(h,g,5)
mynetwork.nodes[h].updateCost(h,f,0)

mynetwork.print()
mynetwork.sendVectorToNeighbors(a)
mynetwork.print()


