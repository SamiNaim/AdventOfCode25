from functools import lru_cache

machines = {}

def count_paths(graph, start, target):

    @lru_cache(None)
    def dfs(node, visited_dac, visited_fft):
        if node == "dac":
            visited_dac = True
        elif node == "fft":
            visited_fft = True
        if node == target and visited_dac and visited_fft:
            return 1
        return sum(dfs(child, visited_dac, visited_fft) for child in graph.get(node, []))

    return dfs(start, False, False)

with open("input11.txt", "r") as f:
    for line in f:
        line = line.strip()
        machine_name = line[:3]
        machine_children = without_first_five = line[5:].split()
        machines[machine_name] = machine_children

count = count_paths(machines, "svr", "out")
print(count, "paths from svr to out visit both dac and fft")