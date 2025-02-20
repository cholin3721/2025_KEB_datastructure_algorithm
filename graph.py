class Graph:
	def __init__(self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(name_ary[v], end =' ')
    print()
    for row in range(g.SIZE) :
        print(name_ary[row], end =' ')
        for col in range(g.SIZE) :
            #print("%2d" % g.graph[row][col], end = ' ')
            print(f"{g.graph[row][col]:2}", end=' ')  #:2 이건 공백용, 슬라이싱이랑 햇갈리지 말기
        print()
    print()



def find_vertex(g, current, find_vtx, visited) -> bool:
    visited.append(current)

    if current == find_vtx:
        return True
    for vertex in range(len(g.SIZE)):
        if g.graph[current][vertex] == 1 and vertex not in visited:
            (g, vertex, find_vtx, visited)

    return False

# visited_ary = [0 for _ in range(len(g))]
# def find_vertex(g, i, find_vtx)
    # global visited_ary
    # visited_ary[i] = 1
    # for j in range(len(g)):
    #     if g[i][j] == 1 and not visited_ary[j]:
    #         find_vertex(g, j, find_vtx)
    #
    # search_result = [name_ary[i] for i, _ in enumerate(visited_ary) if visited_ary[i] == 1]
    # if find_vtx in search_result :
    #     print("찾았습니다")

    #내가 만든거 위에꺼

	# stack = []
	# visited_ary = []
    #
	# current = 0
	# stack.append(current)
	# visited_ary.append(current)
    #
	# while len(stack) != 0:
	# 	next = None
	# 	for vertex in range(g_size) :
	# 		if g.graph[current][vertex] != 0 :
	# 			if vertex in visited_ary :
	# 				pass
	# 			else :
	# 				next = vertex
	# 				break
	# 	if next is not None:
	# 		current = next
	# 		stack.append(current)
	# 		visited_ary.append(current)
	# 	else :
	# 		current = stack.pop()
	# if find_vtx in visited_ary :
	# 	return True
	# else :
	# 	return False


G1 = None
name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

g_size = 6
G1 = Graph(g_size)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print_graph(G1)

# 간선 목록 만들기 [가중치, 시작도시, 도착도시]
edge_ary = []
for i in range(g_size) :
	for k in range(g_size) :
		if G1.graph[i][k] != 0 :
			edge_ary.append([G1.graph[i][k], i, k])

print(edge_ary, len(edge_ary))

# 가중치 순으로 목록 정렬 (내림차순)
# from operator import itemgetter
# edge_ary = sorted(edge_ary, key = itemgetter(0), reverse = True)
edge_ary.sort(reverse = True)


print(edge_ary, len(edge_ary))

# 중복 간선 제거
new_ary = []
for i in range(0, len(edge_ary), 2) :
	new_ary.append(edge_ary[i])

print(new_ary, len(new_ary))

index = 0
while len(new_ary) > g_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
	start = new_ary[index][1]
	end = new_ary[index][2]
	saveCost = new_ary[index][0]

	G1.graph[start][end] = 0
	G1.graph[end][start] = 0

	startYN = find_vertex(G1, start)
	endYN = find_vertex(G1, end)

	if startYN and endYN :
		del new_ary[index]
	else :
		G1.graph[start][end] = saveCost
		G1.graph[end][start] = saveCost
		index += 1

print_graph(G1)