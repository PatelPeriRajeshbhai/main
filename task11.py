# 5.2 Queue Implementation
queue = []

queue.append("A")
queue.append("B")
queue.append("C")
print("stack:",queue)

queue.pop(0)
print("stack:",queue)

element =queue[0]
print("Stack:",element)

poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

empty = not bool(queue)
print("Stack:",empty)

print("Size:",len(queue))

