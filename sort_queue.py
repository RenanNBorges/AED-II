from fila_encadeada import DynamicQueue
from pilha_encadeada import DynamicStack


def sorting_queue(queue_unorganized: DynamicQueue):
    queue_unorganized = queue_unorganized
    s_sorted = DynamicStack()
    s_assistant = DynamicStack()

    while not(queue_unorganized.is_empty()):
        if (s_sorted.is_empty() and s_assistant.is_empty()) or queue_unorganized.peek() < s_sorted.peek():
            s_sorted.push(queue_unorganized.peek())
            queue_unorganized.remove()
        elif queue_unorganized.peek() > s_sorted:
            pass




queue = DynamicQueue()
queue.insert(10)
sorting_queue(queue)


