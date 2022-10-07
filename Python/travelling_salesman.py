from sys import maxsize
from itertools import permutations

V = 4


def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize

    all_perm = list(permutations(vertex))
    all_perm.append(vertex)

    for j in range(len(all_perm)):
        current_pathweight = 0
        k = s
        vertex = all_perm[j]
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]

        current_pathweight += graph[k][s]

        min_path = min(min_path, current_pathweight)

    return min_path


graph = [[0, 10, 15, 20], [10, 0, 35, 25],
         [15, 35, 0, 30], [20, 25, 30, 0]]
# s = int(input())
s = 1
print(travellingSalesmanProblem(graph, s))


