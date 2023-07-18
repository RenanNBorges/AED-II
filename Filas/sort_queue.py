from Filas.fila_encadeada import DynamicQueue
from Pilhas.pilha_encadeada import DynamicStack


def sorting_queue(queue_unorganized: DynamicQueue):
    queue_unorganized = queue_unorganized
    s_sorted = DynamicStack()
    s_assistant = DynamicStack()

    while not(queue_unorganized.is_empty()):
        if (s_sorted.is_empty()) or queue_unorganized.peek() <= s_sorted.peek():
            s_sorted.push(queue_unorganized.peek())
            queue_unorganized.remove()
            while not(s_assistant.is_empty()):
                s_sorted.push(s_assistant.peek())
                s_assistant.pop()

        elif queue_unorganized.peek() > s_sorted.peek():
            s_assistant.push(s_sorted.peek())
            s_sorted.pop()
    while not(s_sorted.is_empty()):
        queue_unorganized.insert(s_sorted.peek())
        s_sorted.pop()
    return queue_unorganized





queue = DynamicQueue()
queue.insert(10)
queue.insert(1)
queue.insert(8)
queue.insert(3)
queue.insert(5)
queue.insert(10)
queue.insert(1)
queue.insert(8)
queue.insert(3)
queue.insert(50)
print(queue)
print(sorting_queue(queue))


