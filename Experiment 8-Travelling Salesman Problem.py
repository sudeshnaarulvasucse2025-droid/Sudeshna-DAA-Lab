import heapq
import time
from itertools import permutations

INF = float('inf')

def reduce_matrix(mat):
    import copy
    m = [row[:] for row in mat]
    n = len(m)
    cost = 0
    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min and row_min != INF:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]
    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min and col_min != INF:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min
    return m, cost  

def tsp_brute_force(cost, n):
    """Brute force for verification with performance tracking"""
    start_time = time.perf_counter()
    
    cities = list(range(1, n))
    best_cost = INF
    best_path = None
    paths_checked = 0
    
    for perm in permutations(cities):
        paths_checked += 1
        path = [0] + list(perm) + [0]
        c = sum(cost[path[i]][path[i+1]] for i in range(n))
        if c < best_cost:
            best_cost = c
            best_path = path
            
    elapsed_time = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds
    return best_cost, best_path, elapsed_time, paths_checked

# Data setup
cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]
n = 5
cities = ['A', 'B', 'C', 'D', 'E']

# Execute TSP
best_cost, best_path, elapsed_time, paths_checked = tsp_brute_force(cost, n)

# Display results
print('5-City TSP - Cost Matrix:')
print(f'{"":>4}', ' '.join(f'{c:>5}' for c in cities))
for i, row in enumerate(cost):
    r = ['INF' if x == INF else str(x) for x in row]
    print(f'{cities[i]:>4}', ' '.join(f'{v:>5}' for v in r))

print(f'\nOptimal Tour: {" -> ".join(cities[i] for i in best_path)}')
print(f'Minimum Cost: {best_cost}')

print(f'\nPath verification:')
for i in range(n):
    u, v = best_path[i], best_path[i+1]
    print(f' {cities[u]} -> {cities[v]}: cost = {cost[u][v]}')

# Performance Summary Output
print("\n" + "-" * 35)
print(f'Execution Time:      {elapsed_time:.3f} ms')
print(f'Total Paths Checked: {paths_checked}')
print("-" * 35)
