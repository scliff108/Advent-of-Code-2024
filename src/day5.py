import networkx as nx

DAY = 5
FILENAME = 'input.txt'
PATH = f'data/day{DAY}/{FILENAME}'


def read_input(filename: str) -> tuple[list[tuple[int]], list[list[int]]]:
    rules = []
    pages = []

    rule_flag = True
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line == '':
                rule_flag = False
                continue

            if rule_flag:
                rules.append(tuple(map(int, line.split('|'))))
            else:
                pages.append(list(map(int, line.split(','))))

    return rules, pages


def build_dependencies(rules: list[tuple[int]]) -> dict[int, list[int]]:
    dependencies = dict()
    for x, y in rules:
        if y in dependencies:
            dependencies[y].add(x)
        else:
            dependencies[y] = set([x])
    return dependencies
    

def part1(graph: nx.DiGraph, pages: list[list[int]]) -> int:
    total = 0
    for p_list in pages:
        if nx.is_path(graph, p_list):
            middle = p_list[len(p_list) // 2]
            total += middle
            # print('valid:', p_list, '- middle:', middle)
            
    return total


def part2(graph: nx.DiGraph, pages: list[list[int]]) -> int:
    total = 0
    for p_list in pages:
        if not nx.is_path(graph, p_list):
            # print(p_list)

            # Find invalid nodes
            valid_nodes = []
            invalid_nodes = []
            n = 1
            while n < len(p_list)+1:
                if nx.is_path(graph, p_list[:n+1]):
                    # print('valid:', p_list[n-1])
                    valid_nodes.append(p_list[n-1])
                    n += 1
                else:
                    # print('invalid:', p_list[n-1])
                    invalid_nodes.append(p_list[n-1])
                    del p_list[n-1]
            
            for node in invalid_nodes:
                n = 0
                while n < len(valid_nodes):
                    # print('start:', valid_nodes)
                    new_path = valid_nodes[:n] + [node] + valid_nodes[n:]
                    if nx.is_path(graph, new_path):
                        # print('insert:', valid_nodes)
                        valid_nodes.insert(n, node)
                        break
                    elif n == len(valid_nodes) - 1:
                        # print('append:', valid_nodes)
                        valid_nodes.append(node)
                        break
                    else:
                        n += 1
            # print('end:', valid_nodes)
            # print('invalid count:', len(invalid_nodes))
            # print()
            middle = valid_nodes[len(valid_nodes) // 2]
            total += middle
    return total


def main():
    rules, pages = read_input(PATH)

    # Build the DAG
    dependencies = build_dependencies(rules)
    graph = nx.DiGraph()
    for page, deps in dependencies.items():
        graph.add_node(page)
        for dep in deps:
            graph.add_edge(dep, page)
    
    p1 = part1(graph, pages)
    print('Part 1:', p1)

    p2 = part2(graph, pages)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()