# -*- coding: utf-8 -*-

from random import randint
from numpy import array
import time
import enum

# Using enum class create enumerations
class E(enum.Enum):
   SPARSE     = 0
   DENSE      = 1
   UNORIENTED = 2
   ORIENTED   = 3
   MAX_INT    = 99999999
   
class Graph:
#    numberNodes    : number of nodes on the graph
#    startNode      : start node
#    structureKind  : SPARSE or DENSE
#    unoriented     : UNORIENTED or ORIENTED
    def __init__(self, numberNodes, startNode, structureKind, orientation):
        self.numberNodes   = numberNodes
        self.startNode     = startNode
        self.numberEdges   = 0
        self.structureKind = structureKind
        self.orientation   = orientation
        self.graph         = array([ [None] * numberNodes ] * numberNodes)

    def addEdge(self, frm, to, weight, orientation):
        self.graph[frm][to] = weight
        self.numberEdges   += 1
        
        if (orientation == E.UNORIENTED):
            self.graph[to][frm] = weight
            self.numberEdges += self.numberEdges
    
    def getGraph(self):
                                            
        for i in range(self.numberNodes):
            for j in range(self.numberNodes):
                if i != j:
                    if self.orientation == E.ORIENTED:
                        if self.structureKind == E.SPARSE:
                            
                            edg = 0
                            for e in range(self.numberNodes):
                                if self.graph[i][j] != None:
                                    edg += 1
                                if edg == 2:
                                    break
                            
                            if edg < 2:
                                self.addEdge(i, j, randint(1, 1000), E.ORIENTED)
                            
                        else:
                            self.addEdge(i, j, randint(1, 1000), E.ORIENTED)
                            
                    else:
                        if self.graph[i][j] == None:
                            
                            if self.structureKind == E.SPARSE:
                                edg = 0
                                for e in range(self.numberNodes):
                                    if self.graph[i][j] != None:
                                        edg += 1
                                    if edg == 2:
                                        break
                                
                                if edg < 2:
                                    self.addEdge(i, j, randint(1, 1000), E.ORIENTED)
                            else:

                                self.addEdge(i, j, randint(1, 1000), E.UNORIENTED)

    
        return self


class Prim():
    def __init__(self, graph):
        self.graph = graph

    def minKey(self, nodeKey, exploredNodes):
        minValue = E.MAX_INT.value
        minIndex = -1
        
        for i in range(self.graph.numberNodes):
            if not exploredNodes[i] and (nodeKey[i] < minValue):
                minValue = nodeKey[i]
                minIndex = i
            
        return minIndex
    
    def findRoute(self):
        ret           = array([None] * self.graph.numberNodes)
        nodeKey       = array([E.MAX_INT.value] * self.graph.numberNodes)
        exploredNodes = array([False] * self.graph.numberNodes)
        
        nodeKey[0] = 0
        
        for i in range(self.graph.numberNodes - 1):
            u = self.minKey(nodeKey, exploredNodes)
            exploredNodes[u] = True
        
            for j in range(self.graph.numberNodes):
                if self.graph.graph[u][j] and not exploredNodes[j] and (self.graph.graph[u][j] < nodeKey[j]):
                    ret[j] = u
                    nodeKey[j] = self.graph.graph[u][j]
                

        return ret        
    
    def showResult(self):
        
        res = self.findRoute()
        
        print("from/to      weight")
        for i in range(1, self.graph.numberNodes):
            print(res[i], " - ", i , "       " , self.graph.graph[i][res[i]])
            
    	

        
class Djikstra():
    def __init__(self, graph):
        self.graph = graph

    def minDist(self, nodeKey, exploredNodes):
        minValue = E.MAX_INT.value
        minIndex = -1
        
        for i in range(self.graph.numberNodes):
            if not exploredNodes[i] and (nodeKey[i] <= minValue):
                minValue = nodeKey[i]
                minIndex = i
            
        return minIndex
    
    def findRoute(self):
        ret           = array([E.MAX_INT.value] * self.graph.numberNodes)
        exploredNodes = array([False] * self.graph.numberNodes)
        
        ret[self.graph.startNode] = 0
        
        for i in range(self.graph.numberNodes - 1):
            u = self.minDist(ret, exploredNodes)
            exploredNodes[u] = True
        
            for j in range(self.graph.numberNodes):
                if self.graph.graph[u][j] and not exploredNodes[j] and ret[u] != E.MAX_INT.value and (ret[u] + self.graph.graph[u][j] < ret[j]):

                    ret[j] = ret[u] + self.graph.graph[u][j]
                

        return ret   
            
    
    
    
outLoop = 15
innerLoop = 20
numberOfNodes = 3
structure = E.SPARSE
orientation = E.ORIENTED

#g = Graph(8, 0, structure, E.UNORIENTED)
#
#g.addEdge(0, 1, 14, E.UNORIENTED)
#g.addEdge(0, 2, 3, E.UNORIENTED)
#g.addEdge(1, 3, 6, E.UNORIENTED)
#g.addEdge(1, 2, 10, E.UNORIENTED)
#g.addEdge(1, 4, 5, E.UNORIENTED)
#g.addEdge(2, 5, 8, E.UNORIENTED)
#g.addEdge(3, 4, 4, E.UNORIENTED)
#g.addEdge(4, 5, 2, E.UNORIENTED)
#g.addEdge(4, 6, 9, E.UNORIENTED)
#g.addEdge(5, 7, 15, E.UNORIENTED)
#
#print(g.graph)
#
#Prim(g).showResult()

#p = Graph(5, 0, structure, E.ORIENTED)
#
#p.addEdge(0, 1, 10, E.ORIENTED)
#p.addEdge(0, 2, 5, E.ORIENTED)
#p.addEdge(1, 2, 2, E.ORIENTED)
#p.addEdge(1, 3, 1, E.ORIENTED)
#p.addEdge(2, 1, 3, E.ORIENTED)
#p.addEdge(2, 3, 9, E.ORIENTED)
#p.addEdge(2, 4, 2, E.ORIENTED)
#p.addEdge(3, 4, 4, E.ORIENTED)
#p.addEdge(4, 0, 7, E.ORIENTED)
#p.addEdge(4, 3, 6, E.ORIENTED)
#
#print(p.graph)
#
#Djikstra(p).findRoute()


print('Algorithm;NumberOfNodes;TypeGraph;Orientation;Loops;Time')

for i in range(outLoop):
    
    numberOfNodes += 10
    currentGraph = Graph(numberOfNodes, 0, structure, orientation).getGraph()
    
    accTime = 0
    for j in range(innerLoop):
        start = time.time()
        Prim(currentGraph).findRoute()
        end = time.time()
        
        accTime += (end - start)
    print('PRIM;' + str(numberOfNodes) + ';' + structure.name + ';' + orientation.name + ';' + str(innerLoop) + ';' + str(accTime))

    accTime = 0
    for j in range(innerLoop):
        start = time.time()
        Djikstra(currentGraph).findRoute()
        end = time.time()
        
        accTime += (end - start)
    print('DJIKSTRA;' + str(numberOfNodes) + ';' + structure.name + ';' + orientation.name + ';' + str(innerLoop) + ';' + str(accTime))





        