from functools import lru_cache

machines = {}

def count_paths(graph, start, target):

    @lru_cache(None)
    def dfs(node):
        if node == target:
            return 1
        return sum(dfs(child) for child in graph.get(node, []))

    return dfs(start)

with open("input11.txt", "r") as f:
    for line in f:
        line = line.strip()
        machine_name = line[:3]
        machine_children = without_first_five = line[5:].split()
        machines[machine_name] = machine_children

count = count_paths(machines, "you", "out")
print(count, "different paths leading from you to out")