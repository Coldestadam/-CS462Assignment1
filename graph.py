import numpy as np
### graph.py
### an implementation of a graph using an adjacency list.

## helper class representing a node in a graph. For the moment, nodes
## only have names. Later, we will add state variables.

class Node() :
    def __init__(self, n):
        self.name = n

    def __hash__(self):
        return hash(self.name)

### an edge is a link between two nodes. Right now, the only other
### information an edge carries is the weight of the link. Later we
### will add other annotations.

class Edge() :
    def __init__(self, src,dest, weight) :
        self.src = src
        self.dest = dest
        self.weight = weight

### The graph class itself.
### The nodeTable is a dictionary that maps names to Node objects.
### (this keeps us from having to repeatedly search edgeMap.keys())

### The edgeMap is a dictionary that maps nodes to lists of Edges emanating from that node.

class Graph() :

    def __init__(self):
        self.nodeTable = {}
        self.edgeMap = {}

    ### implements the 'in' keyword. Returns true if the node is in the graph.
    def __contains__(self, item):
        return item in self.nodeTable

    def getNode(self, src):
        return self.nodeTable[src]

    def addNode(self, src):
        if src not in self.nodeTable :
            self.nodeTable[src] = Node(src)

    def addEdge(self, src, dest, weight):
        e = Edge(src,dest,weight)
        self.addNode(src)
        self.addNode(dest)
        if src in self.edgeMap :
            self.edgeMap[src].append(e)
        else :
            self.edgeMap[src] = [e]


    ## Assume file is in the mtx format: % is a comment
    ## Otherwise it's source destination weight
    ### The file in the github repo will work as a sample for you.
    ### It's in the format: source, vertex, weight. You should assume that the graph is symmetric -
    ### if there's an edge from a to b, there's an edge from b to a.
    ### You can find lots of others here: http://networkrepository.com/index.php
    def readFromFile(self, fname):
        with open(fname) as f :
            for l in f.readlines() :
                if not l.startswith("%") :
                    (s,d,w) = l.split()
                    self.addEdge(s,d,w)

    ### inputs are the name of a startNode and endNode. Given this,
    ### return a list of Nodes that indicates the path from start to finish, using breadth-first search.

    def breadthFirstSearch(self, startNode, endNode):
        path = []
        node = self.nodeTable[startNode]
        queue = [node]
        
        while len(queue) > 0:
            node = queue.pop(0)
            path.append(node)

            if node.name == endNode:
                return path
            else:
                for edge in self.edgeMap[node.name]:
                    child = self.getNode(edge.dest)
                    if child not in queue:
                        queue.append(child)
            
        return path

    ### inputs are the name of a startNode and endNode. Given this,
    ### return a list of Nodes that indicates the path from start to finish, using depth-first search.

    def depthFirstSearch(self, startNode, endNode):
        path = []
        node = self.nodeTable[startNode]
        stack = [node]

        while True:
            node = stack.pop()
            path.append(node)

            if node.name == endNode:
                return path
            
            else:
                for edge in self.edgeMap[node.name]:
                    child = self.getNode(edge.dest)
                    stack.append(child)


    ### implement Djikstra's all-pairs shortest-path algorithm.
    ### https://yourbasic.org/algorithms/graph/#dijkstra-s-algorithm
    ### return the array of distances and the array previous nodes.

    def djikstra(self, startNode):
        dist = np.zeros(len(self.nodeTable))
        prev = np.zeros(len(self.nodeTable))

        # Set of all the nodes
        Q = []
        for nodeName in self.nodeTable.keys():
            # nodeNames are integers from 1 to 16, so I will attach an idx to each one
            idx = int(nodeName) - 1 #Converting to integers since all data was stored as strings in the graph
            dist[idx] = np.inf
            prev[idx] = None
            Q.append(self.getNode(nodeName))
        
        dist[int(startNode)-1] = 0

        while len(Q) > 0:
            node = Q.pop()

            for edge in self.edgeMap[node.name]:
                child = self.getNode(edge.dest)
                alt = dist[int(node.name)-1] + int(edge.weight)
                if alt < dist[int(child.name)-1]:
                    dist[int(child.name)-1] = alt
                    prev[int(child.name)-1] = int(node.name)

        return dist, prev

    ### takes as input a starting node, and computes the minimum spanning tree, using Prim's algorithm.
    ### https:// en.wikipedia.org/wiki/Prim % 27s_algorithm
    ### you should return a new graph representing the spanning tree generated by Prim's.

    # Created this function to return the edge of to vertices in the graph
    def find_edge(u, v):
        for edge in self.edgeMap[u]:
            if edge.dest == v:
                return edge
            
    def prim(self, startNode):
        reached = [startNode]
        unreached = [nodeName for nodeName in self.nodeTable]
        unreached.remove(startNode)

        # Creating the tree using a graph
        tree = Graph()

        while len(unreached) > 0:
            lowest_edge_weight = np.inf
            u_low = None
            v_low = None
            for u in reached:
                for j in unreached:
                    edge = find_edge(u, v)
                    if int(edge.weight) < lowest_edge_weight:
                        lowest_edge_weight = int(edge.weight)
                        u_low = u
                        v_low = v
            tree.addEdge(u_low, v_low, lowest_edge_weight)
            reached.append(v_low)
            unreached.remove(v_low)

        return tree

    ### 686 students only ###
    ### takes as input a startingNode and returns a list of all nodes in the maximum clique containing this node.
    ### https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique

    def clique(self, startNode):
        pass