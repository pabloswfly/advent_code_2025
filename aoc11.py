from collections import defaultdict


file_path = "data/aoc11.txt"

ex1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

ex2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


def process_text(file: str) -> dict:
    graph = defaultdict(list)

    for line in file.split("\n"):
        if line:
            node, connections = line.rstrip().split(":")
            graph[node] = [n for n in connections.strip().split(" ") if n != ""]

    return graph


def dfs(node: str, graph: dict, n_routes: dict) -> int:
    if node in n_routes:
        return n_routes[node]

    if node == "out":
        return 1

    res = 0

    for child in graph[node]:
        res += dfs(child, graph, n_routes)

    n_routes[node] = res

    return res


def dfs_paths(start: str, graph: dict) -> int:
    memory = {}

    def dfs2(node: str, has_dac: bool, has_fft: bool) -> int:
        key = (node, has_dac, has_fft)

        if key in memory:
            return memory[key]

        if node == "out":
            return 1 if has_dac and has_fft else 0

        has_dac = has_dac or node == "dac"
        has_fft = has_fft or node == "fft"

        res = 0
        for child in graph[node]:
            res += dfs2(child, has_dac, has_fft)

        memory[key] = res

        return res

    return dfs2(start, False, False)


#################### TASK 1 ####################

with open(file_path, "r") as file:
    graph = process_text(ex1)
    # graph = process_text(file.read())

n_routes = defaultdict(int)
print(dfs("you", graph, n_routes))

#################### TASK 2 ####################

with open(file_path, "r") as file:
    # graph = process_text(ex2)
    graph = process_text(file.read())


print(dfs_paths("svr", graph))
