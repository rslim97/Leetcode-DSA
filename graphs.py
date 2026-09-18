from collections import deque

graph={
    "A":["B"],
    "B":["A","C","H"],
    "C":["B","D"],
    "H":["B","J"],
    "D":["C"],
    "J":["H"]
}

"""
In adjacency lists, use graph[node]
to get children at each node.
"""

# BFS

# def bfs(graph,root):
#     queue=deque([root])
#     visited=set()
#     while queue:
#         node=queue.popleft()
#         # Check if node is visited
#         if node in visited:
#             continue
#         # Mark node as visited
#         visited.add(node)
#         for c in graph[node]:
#             queue.append(c)

#     return visited

# def bfs(graph,root):
#     queue=deque([root])
#     visited=set()
#     while queue:
#         node=queue.popleft()
#         if node not in visited:
#             visited.add(node)
#             # queue+=graph[node]
#             for child in graph[node]:
#                 queue.append(child)

#     return visited

# # Slightly more optimal:
# # Mark is visited before adding to queue
def bfs(graph,root):
    queue=deque([root])
    visited=set(root)
    while queue:
        node=queue.popleft()
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return visited

# DFS

# def dfs(graph,root):
#     stack=deque([root])
#     visited=set()
#     while stack:
#         node=stack.pop()
#         # Check if node is visited
#         if node in visited:
#             continue
#         # Mark node as visited
#         visited.add(node)
#         for c in graph[node]:
#             stack.append(c)

#     return visited

# def dfs(graph,root):
#     stack=deque([root])
#     visited=set()
#     while stack:
#         node=stack.pop()
#         if node not in visited:
#             visited.add(node)
#             for child in graph[node]:
#                 stack.append(child)

#     return visited

# # # Slightly more optimal:
# # # Mark is visited before adding to stack
# def dfs(graph,root):
#     stack=deque([root])
#     visited=set(root)
#     while stack:
#         node=stack.pop()
#         for child in graph[node]:
#             if child not in visited:
#                 visited.add(child)
#                 stack.append(child)

#     return visited

# DFS recursive
def dfs(graph,root):
    visited=set()
    def helper(node,visited):
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                helper(child,visited)

    helper(root,visited)
    return visited 


if __name__ == '__main__':
    res=bfs(graph,"A")
    print(res)
    res=dfs(graph,"A")
    print(res)
