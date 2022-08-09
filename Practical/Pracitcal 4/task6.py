
from collections import deque
from queue import Queue

d = deque()
d.extend(a for a in range(1, 9))

q = Queue()
q.put(d.popleft())
q.put(d.popleft())
q.put(d.popleft())

d.append(d.popleft())
q.put(d.popleft())
q.put(d.pop())

q.put(d.popleft())
q.put(d.popleft())
q.put(d.popleft())

l = [val for val in q.queue]
print(l)



