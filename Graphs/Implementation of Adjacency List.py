from collections import defaultdict

class Graph:

    def __init__(self):
        self.vertices = defaultdict(list)   #             <-IMPORTANT->
                                            # This approach is used when there is no
    def addEdge(self, u, v):                # weights on the edges or we can say vertices
        self.vertices[u].append(v)          # are just simply connected
        self.vertices[v].append(u)
    def __str__(self):
        return str(self.vertices)


#                   <-IMPORTANT->
# The approach given below is used when edges have weight,
# it maintains a list of neighbors and the cost to go to
# that neighbor. Note that this approach can be used even when
# the edges don't have any weight (default weight = 0)

class Vertex:
    # issme dictionary has key as Vertex object address and value is weight of the edge connecting to that neighbor
    # here all the objects of class Vertex will have their own
    # dictionary associated with each object with keys as
    # neighbor object (nbr object is also a vertex class object)
    # and value as weight of edge connecting to that nbr
    def __init__(self,data):
        self.data = data
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight  # key is vertex object and value is weight

    def __str__(self):  # this defines what happens if we print(object_of_Vertex_class)
        return str(self.data) + ' connected to ' + str([x.data for x in self.connectedTo])  # this will run if we print an object of class Vertex

    def getConnections(self):
        return self.connectedTo.keys()

    def getData(self):
        return self.data

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:    # issme dictionary has key as data and value as Vertex object address
    # here each object of class Graph will have have a dictionary associated
    # in which key is data and value is vertex
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertices(self,data): # this makes an object of class Vertex and adds that to verList as a value and key is its data
        self.numVertices += 1
        newVertex = Vertex(data)
        self.vertList[data] = newVertex

    def getVertex(self,n):  # this takes data as argument and returns object address of Vertex class
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertices(f)
        if t not in self.vertList:
            self.addVertices(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)  # vertList[f] will return object of class Vertex then we use its method to add a neighbour

    def __iter__(self):
        return iter(self.vertList.values())  # now we can use "for item in object_of_this_class"

g = Graph()
g.addVertices(99)
g.addVertices(98)
g.addVertices(97)
g.addVertices(96)
g.addEdge(99,98,10)
for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print("")