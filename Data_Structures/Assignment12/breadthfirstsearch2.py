import linkedliststackqueue2, turtle

class Vertex:
	def __init__(self,vertexId,x,y,label):
		self.vertexId = vertexId
		self.x = x
		self.y = y
		self.label = label
		self.adjacentTo = []
		self.path = -1
        
class Edge:
	def __init__(self,v1,v2,weight,label):
		self.v1 = v1
		self.v2 = v2
		self.weight = weight
		self.label = label

vertexList = []
edgeList = []
visited = set()
finalPath = []

def readGraph():
	file = open("roadGraph.txt", "r")
	N,L = file.readline().strip().split("\t")
	for i in range(int(N)):
		label,y,x = file.readline().strip().split("\t")
		vertexList.append(Vertex(i,float(x),float(y),label))
	for line in file:
		v1,v2,miles,road = line.strip().split("\t")
		edgeList.append(Edge(int(v1), int(v2), int(miles), road))
	file.close()

def addNeighbors():
	for edge in edgeList:
		vertexList[edge.v1].adjacentTo.append(edge.v2)
		vertexList[edge.v2].adjacentTo.append(edge.v1)

def breadthfirstsearch(source, destination):
	start = vertexList[source]
	goal = vertexList[destination]
	queue = linkedliststackqueue2.Queue()
	queue.enqueue([start])
	while not queue.isEmpty():
		path = queue.dequeue()
		current = path[0]
		if not current in visited:
			visited.add(current)
			if current == goal:
				for vertex in path:
					finalPath.append(vertex)
					print(vertex.label)
				print('path length from', goal.label, 'to', start.label, '=', len(path)-1)

				return
			for v in current.adjacentTo:
				adjacent = vertexList[v]
				if not adjacent in path:
					queue.enqueue([adjacent]+path)

def showGraph():
	t = turtle.Turtle()
	t.ht()
	turtle.tracer(0, 0)
	screen = t.getscreen()
	minx = 1000.0
	maxx = -1000.0
	miny = 1000.0
	maxy = -1000.0
	for vertex in vertexList:
		if vertex.x > maxx:
			maxx = vertex.x
		if vertex.x < minx:
			minx = vertex.x
		if vertex.y > maxy:
			maxy = vertex.y
		if vertex.y < miny:
			miny = vertex.y
	ax = 560.0 /(maxx - minx)
	bx = -280.0 - ax * minx
	ay = 560.0 /(maxy - miny)
	by = -280.0 - ay * miny
	for vertex in vertexList:
		t.penup()
		t.goto(vertex.x * ax + bx,vertex.y * ay + by)
		t.pendown()
		if vertex in finalPath:
			t.color('black')
			if vertex == finalPath[0] or vertex == finalPath[len(finalPath) - 1]:
				t.color('red')
		elif vertex in visited:
			t.color('orange')
		else:
			t.color('gray')
		t.write(vertex.label,align="center",font=("Arial",7,"bold"))
	for edge in edgeList:
		t.color('gray')
		if vertexList[edge.v1] in finalPath and vertexList[edge.v2] in finalPath:
			for i in range(len(finalPath) - 1):
				if vertexList[edge.v1] == finalPath[i] and vertexList[edge.v2] == finalPath[i + 1]:
					t.color('red')
					break
				if vertexList[edge.v2] == finalPath[i] and vertexList[edge.v1] == finalPath[i + 1]:
					t.color('red')
					break
		t.penup()
		x1 = vertexList[edge.v1].x * ax + bx
		y1 = vertexList[edge.v1].y * ay + by
		x2 = vertexList[edge.v2].x * ax + bx
		y2 = vertexList[edge.v2].y * ay + by
		t.goto(x1,y1)
		t.pendown()
		t.goto(x2,y2)		
	t.ht()
	screen.exitonclick()
	print("Program Execution Completed.")

def binarySearch(label):
	lo = 0
	hi = len(vertexList) - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		if label == vertexList[mid].label:
			return mid
		if label < vertexList[mid].label:
			hi = mid - 1
		else:
			lo = mid + 1
	return -1

def getLocation(locationType):
	while True:
		location = input('Enter a ' + locationType + ': ')
		if len(location) < 1:
			return -1
		index = binarySearch(location)
		if index >= 0:
			return index
		else:
			print("no such location")
	return -1


def main():
	readGraph()
	addNeighbors()
	source = getLocation('source')
	if source < 0:
		return
	destination = getLocation('destination')
	if destination < 0:
		return
	breadthfirstsearch(source, destination)
	showGraph()

if __name__ == "__main__":
	main()
