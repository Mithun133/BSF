# Implementesion of BSF using python

def bsf(graph, node, visited, queue, level):
    visited.append(node)
    queue.append(node)
    level[node] = 0

    while queue:
        parent = queue.pop(0)
        print(parent, end=' ')

        for child in graph[parent]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
                level[child] = level[parent] + 1




if __name__ == '__main__':

    visited = []
    queue = []
    level = {}
    graph = {
        '1' : ['2', '4', '3'],
        '2' : ['6'],
        '4' : ['7'],
        '3' : ['8'],
        '6' : ['10'],
        '7' : ['9'],
        '8' : ['5'],
        '10' : [],
        '9'  : [],
        '5'  : []

    }
bsf(graph, '1', visited, queue, level)
print()
print(level)