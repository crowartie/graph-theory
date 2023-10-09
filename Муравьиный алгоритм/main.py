import random


graph = {
    1: [(2, 10), (3, 6), (4, 8)],
    2: [(4, 5), (7, 11)],
    3: [(5, 3)],
    4: [(3, 2), (5, 5), (6, 7), (7, 12)],
    5: [(6, 9), (9, 12)],
    6: [(8, 8), (9, 10)],
    7: [(6, 4), (8, 6)],
    8: [(9, 1)],
    9: []
}


def select_next_city(graph, current_city, visited_cities, pheromone):
    cities = set(c for c, _ in graph[current_city]) - set(visited_cities)
    if not cities:
        return random.choice(list(set(graph.keys()) - set(visited_cities)))
    probabilities = []
    for city in cities:
        numerator = pheromone[(current_city, city)]
        denominator = 0
        for c in cities:
            denominator += pheromone[(current_city, c)]
        probability = numerator / denominator
        probabilities.append(probability)
    return random.choices(list(cities), probabilities)[0]


def update_pheromones(pheromone, all_paths, decay=0.1):
    for k, v in pheromone.items():
        pheromone[k] = v * (1.0 - decay)
    for path, cost in all_paths:
        for i in range(len(path) - 1):
            if (path[i], path[i + 1]) in pheromone and cost != 0:
                pheromone[(path[i], path[i + 1])] += 1.0 / cost
    return pheromone


def path_cost(path):
    if len(path) < 2:
        return 0
    total_cost = 0
    for i in range(1, len(path)):
        cost_found = False
        for city, cost in graph[path[i - 1]]:
            if city == path[i]:
                total_cost += cost
                cost_found = True
                break
        if not cost_found:
            total_cost += 0
    return total_cost

def ant_algorithm(graph, num_ants, num_iterations):
    pheromone = {}
    for city1 in graph:
        for city2, _ in graph[city1]:
            pheromone[(city1, city2)] = 1
    best_path = None
    all_paths = []

    for _ in range(num_iterations):
        for _ in range(num_ants):
            path = [random.choice(list(graph.keys()))]
            while len(path) < len(graph):
                next_city = select_next_city(graph, path[-1], path, pheromone)
                if next_city is None:
                    break
                path.append(next_city)
            if (path[-1], path[0]) not in pheromone:
                continue
            all_paths.append((path, path_cost(path)))
        pheromone = update_pheromones(pheromone, all_paths)

    return min(all_paths, key=lambda x: x[1])


if __name__ == "__main__":
    print(ant_algorithm(graph, len(graph), 1000))

