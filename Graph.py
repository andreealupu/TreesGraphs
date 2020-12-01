#set of values that are related 
#nodes connected with edges 
#models: internet, friendships, networks, family, roads, etc 


#Types of Graphs 
'''
directed -> movement is directed 
undirected 

weighted -> edges carry weights 
unweighted 

cyclic -> virtices connected in a cicluar manner 
acyclic 
'''

#Edge List 
graph = [[0,2],[2,3],[2,1],[1,3]]
#adjacent List 
#index of array holds connects 
#can use a key
graph = [[2], [2,3], [0,1,3], [1,2]]

#adjacent Matrix 
graph = {
   1: [0,0,1,0],
    2: [0,0,1,1],
    3: [1,0,1,0],
    4: [0,0,1,0]
}


class Graph: 
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {

        }
    def addVertex(self,node):
        self.numberOfNodes += 1
        self.adjacentList[node] = []

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        allNodes = self.adjacentList
        for i in allNodes:
            nodeConnections = self.adjacentList[i]
            connections = ""
            for vertex in nodeConnections:
                connections += vertex + " "
            print(i + "--> " + connections)

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')

myGraph.showConnections(); 

'''
pros: 
    relationships

cons:
    scaling is hard

'''

