from dataclasses import dataclass
import random
import sys

@dataclass
class Neighbor:
    nr: int
    edge_weight: int

def get_neighbors(node: int):
    print(node)
    sys.stdout.flush()
    response = sys.stdin.readline().split()
    num_neighbors = int(response[0])
    return [Neighbor(int(response[1+2*i]), int(response[1+2*i+1])) for i in range(num_neighbors)]

def msf():
    N = int(sys.stdin.readline())
    W = int(sys.stdin.readline())
    Q = int(sys.stdin.readline())
    neighbor_history = {}
    requests = 0
    b = 0
    b_to_add = 0
    bW = 0
    s = -1
    while True:
        start_node = random.randrange(0, N)
        s += 1
        b += b_to_add
        b_to_add = 0
        for w in range(1, W+1):
            queue = [start_node]
            queue_history = set(queue)
            visited = 0
            visited_limit = 1/random.random()
            while queue and visited <= visited_limit:
                next = queue.pop(0)
                visited += 1
                neighbors = None
                if next in neighbor_history:
                    neighbors = neighbor_history[next]
                else:
                    if requests == Q:
                        cW = bW*N/s
                        print(f"end {(N+b*N/s-cW*(W+1))}")
                        return
                    neighbors = get_neighbors(next)
                    neighbor_history[next] = neighbors
                    requests += 1
                for neighbor in neighbors:
                    if neighbor.edge_weight <= w and neighbor.nr not in queue_history:
                        queue.append(neighbor.nr)
                        queue_history.add(neighbor.nr)
            if visited <= visited_limit:
                b_to_add += 1
                if w == W:
                    bW += 1
                    
if __name__ == "__main__":
    random.seed(12)
    msf()