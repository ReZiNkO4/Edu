from collections import deque


class Graph:

    def __init__(self, capacity):
        self.capacity = capacity
        self.n = len(capacity)

    def bfs(self, source, sink, parent):
        visited = [False] * self.n
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in range(self.n):
                if not visited[v] and self.capacity[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True

        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.n
        max_flow = 0
        step = 1

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[parent[s]][s])
                s = parent[s]

            path = []
            v = sink

            while v != source:
                path.append(v)
                v = parent[v]

            path.append(source)
            path.reverse()
            letter_path = [chr(65 + v) for v in path]
            print(f"\nШаг {step}")
            print("Найден путь:", " -> ".join(letter_path))
            print("Поток через путь:", path_flow)

            max_flow += path_flow

            print("Текущий максимальный поток:", max_flow)
            v = sink

            while v != source:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                v = parent[v]

            step += 1

        return max_flow

if __name__ == "__main__":
    capacity = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    g = Graph(capacity)
    max_flow = g.ford_fulkerson(0, 10)
    print("\nМаксимальный поток:", max_flow)