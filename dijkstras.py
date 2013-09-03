N = 200
visited = [-1] * N
inf = 1000000
distance = []

for i in range(N):
	distance.append([])
	for j in range(N):
		distance[i].append(inf)

def  unVisited():
	X = []
	Y = []
	for i in range(N):
		if visited[node] >= 0: 
			X.append(i)
		else:
			Y.append(i)
	return [X,Y]

def dijkstraAlgo():
	visited[0] = 0 
	X,Y = unVisited()

	while len(Y)!=0 :
		min_dis = 1000000
		for i in X:
			for j in Y:
				curr = visited[i] + distance[i][j]
				if curr < min_dis:
					min_dis = curr 
					min_node = j
		visited[min_node]=min_dis
		X,Y = unVisited()

def main():
	fp = open('dijkstraData.txt','r')
	for line in fp:
		row = line.strip().split('\t')
		for val in row[1:]:
			node,dist = val.split(',')
			distance[int(row[0]) - 1][int(node) - 1] = int(dist)

	fp.close()
	dijkstraAlgo()
	res = [7,37,59,82,99,115,133,165,188,197]
	final_res = []
	for i in res:
		final_res.append(str(visited[i - 1]))
	print ",".join(final_res)


if __name__ == "__main__":
	main()