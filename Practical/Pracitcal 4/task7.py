
from collections import deque
from queue import LifoQueue

r = deque()
r.extend(a for a in range(1, 9))

S = LifoQueue()
print(r.popleft())
print(r.popleft())
print(r.popleft())

S.put(r.popleft())
print(r.popleft())
print(S.get())

print(r.popleft())
print(r.popleft())
print(r.popleft())

