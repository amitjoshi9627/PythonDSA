class Graph:
	graph_dict = {}

	def addEdge(self,node,neighbour):
		if node in self.graph_dict:
			self.graph_dict[node].append(neighbour)
		else:
			self.graph_dict[node] = [neighbour]

	def showEdges(self):

		for node in self.graph_dict:
			print(f"{node}: {self.graph_dict[node]}")

	def find_path(self,start,end,path = []):
		path = path + [start]

		if start == end:
			return path
		if start not in self.graph_dict:
			return None

		for node in self.graph_dict[start]:

			if node not in path:
				newPath = self.find_path(node,end,path)

				if newPath:
					return newPath
		return None


	def find_all_paths(self,start,end,path = []):
		path = path + [start]
		if start == end:
			return [path]
		if not start in self.graph_dict:
			return []
		paths = []

		for node in self.graph_dict[start]:

			if node not in path:
				newPaths = self.find_all_paths(node,end,path)
				for newPath in newPaths:
					paths .append(newPath)
		return paths			

	def shortest_path(self,start,end,path = []):

		path = path+[start]

		if start == end:
			return path

		if start not in self.graph_dict:
			return None

		shortest = None

		for node in self.graph_dict[start]:

			if node not in path:

				newPath = self.shortest_path(node,end,path)

				if newPath:
					if not shortest or len(newPath) < len(shortest):
						shortest = newPath
		return shortest
	def shortest_path_efficient(self,start,end):

		dist = {start:[start]}

		q = [start]

		while len(q):
			a = q.pop(0)

			for node in self.graph_dict[a]:

				if node not in dist:
					dist[node] = dist[a] + [node]
					q.append(node)
		return dist[end]

	def bfs(self,start):

		q = [start]
		
		visited = {}

		while len(q):
			node = q.pop(0)
			print(node,end=' ')
			visited[node] = True
			for n in self.graph_dict[node]:
				if n not in visited:
					q.append(n)
					visited[n] = True
	def dfs(self,start,visited={}):
		q = [start]
		visited[start] = True
		# if q == []:
			# return
		# node = q.pop(-1)
		print(start,end=' ')
		for n in self.graph_dict[start]:
			if n not in visited:
				self.dfs(n,visited)



g= Graph()
g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('2', '3')
g.addEdge('2', '1')
g.addEdge('3', '1')
g.addEdge('3', '2')
g.addEdge('3', '4')
g.addEdge('4', '3')
g.showEdges()

print(g.find_path('1','4'))

print(g.find_all_paths('1','4'))

print(g.shortest_path('1','4'))

print(g.shortest_path_efficient('1','4'))

g.bfs('1')
print()
g.dfs('1')