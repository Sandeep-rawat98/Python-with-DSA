"""
Deque not queue , a collection where tc for pop and push is O(1) and is efficient
"""

from collections import deque

q = deque()
print(q)
q.append(100)
q.append(200)
print(q)
q.appendleft(300)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
