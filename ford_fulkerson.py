import timeit
from collections import defaultdict

class Graph:

	def __init__(self, graph):
		self.graph = graph 
		self. ROW = len(graph)
		
	def BFS(self, s, t, parent):

		# Marquer tous les sommets comme non visités
		visited = [False]*(self.ROW)
		queue = []
		queue.append(s)
		visited[s] = True

		while queue:
			u = queue.pop(0)

			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0:
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
					if ind == t:
						return True

		return False
			
	
	# Renvoie le débit maximal de s à t 
	def FordFulkerson(self, source, sink):
		parent = [-1]*(self.ROW)
		max_flow = 0 

		#Augmenter le flux tant qu'il y a un chemin de la source au puits
		while self.BFS(source, sink, parent) :
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Ajouter le flux de chemin au flux global
			max_flow += path_flow

			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow


#Test

graph = [[0, 5, 27, 0, 0, 0],
        [0, 0, 18, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 17],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)
source = 0; sink = 5
 
print ("Le flot maximal est %d " % g.FordFulkerson(source, sink))

# Mesure du temps d'exécution avec timeit
t = timeit.timeit(lambda: Graph(graph), number=1)
print("Durée d'exécution : %.5f secondes" % t)


