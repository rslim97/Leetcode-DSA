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

#------- BFS -------

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

# Mark node as visited directly after pop.
def bfs(graph,root):
    queue=deque([root])
    visited=set()
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.add(node)
            # queue+=graph[node]
            for child in graph[node]:
                queue.append(child)

    return visited

# # Slightly more optimal:
# # 1. Mark node as visited when initializing queue.
# # 2. Mark each child as visited before adding to queue.
# def bfs(graph,root):
#     queue=deque([root])
#     visited=set(root)
#     while queue:
#         node=queue.popleft()
#         for child in graph[node]:
#             if child not in visited:
#                 visited.add(child)
#                 queue.append(child)

#     return visited

#------- DFS -------

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

# Mark node as visited directly after pop.
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

# # Slightly more optimal:
# # 1. Mark node as visited when initializing stack.
# # 2. Mark each child as visited before adding to stack.
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

# DFS recursive:
# This DFS version visits each node based on 
# the total number of ingoing and outgoing edges.
# It is therefore useful to record edges.
def dfs(graph,root):
    visited=set()
    edges=set()
    def helper(node,visited):
        print("node",node)
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                edges.add((child,node))
                helper(child,visited)

    helper(root,visited)
    return visited,edges

# # DFS recursive: 
# # This DFS version visits each node exactly once.
# # https://cseweb.ucsd.edu/~dakane/CSE101LectureArchive/Lec2.pdf
# def dfs(graph,root):
#     visited=set()
#     edges=set()
#     def helper(node,visited):
#         print("node",node)
#         visited.add(node)
#         for child in graph[node]:
#             if child not in visited:
#                 edges.add((child,node))
#                 helper(child,visited)

#     helper(root,visited)
#     return visited,edges 


if __name__ == '__main__':
    res=bfs(graph,"A")
    print(res)
    visited, edges=dfs(graph,"A")
    print("visited",visited)
    print("len(visited)",len(visited))
    print("edges",edges)
    print("len(edges)",len(edges))