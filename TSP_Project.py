from itertools import permutations
import time
import matplotlib.pyplot as plt


def distance_between_two_points(source_point, destination_point):
    result = ((source_point[0] - destination_point[0]) ** 2 + (source_point[1] - destination_point[1]) ** 2) ** (1 / 2)

    return result


def calculate_distances(path):
    result = 0
    for i, point in enumerate(path[0:(len(path) - 1)]):
        result += distance_between_two_points(point, path[i + 1])

    return result


def nearest_neighbor_algorithm(points):
    shortest_path = []
    not_visited = points
    shortest_path.append(points[0])
    not_visited.remove(points[0])

    while len(not_visited) > 0:
        not_visited = sorted(not_visited, key=lambda k: distance_between_two_points(shortest_path[-1], k))
        nearest_neighbor = not_visited[0]
        shortest_path.append(nearest_neighbor)
        not_visited.remove(nearest_neighbor)
    return shortest_path


def exhaustive_algorithm(points):
    perm = []
    for permutation in permutations(points):
        permutation = list(permutation)
        first = permutation[0]
        permutation.append(first)
        perm.append(permutation)

    perm = sorted(perm, key=calculate_distances)

    # path=perm[0]
    return perm[0]


def run():
    file = open("inputs.txt", "r")
    input_txt = file.readlines()
    points = []
    for i in input_txt:
        points.append(i.split())
    del points[0]
    points = [(float(x), float(y)) for (x, y) in points]
    first_point = points[0]
    start_time = time.clock()
    exhaustive_algorithm_path = exhaustive_algorithm(points)
    exhaustive_algorithm_path_length = calculate_distances(exhaustive_algorithm_path)
    end_time_exhaustive = time.clock() - start_time
    end_time_exhaustive = format(float(end_time_exhaustive), '.11f')
    start_time_2 = time.clock()
    nearest_neighbor_algorithm_path = nearest_neighbor_algorithm(points)
    nearest_neighbor_algorithm_path_length = calculate_distances(nearest_neighbor_algorithm_path)
    nearest_neighbor_algorithm_path_length += distance_between_two_points(nearest_neighbor_algorithm_path[0],
                                                                          nearest_neighbor_algorithm_path[-1])
    end_time_nearest = time.clock() - start_time_2
    end_time_nearest = format(float(end_time_nearest), '.11f')
    nearest_neighbor_algorithm_path.append(first_point)
    print(
        """Nearest Neighbor:\nPath Length: {} \nPath: {} \nRunning Time: {} \n\nOptimal TSP:\nPath Length: {} \nPath: {}\nRunning Time: {} \n"""

            .format(nearest_neighbor_algorithm_path_length,
                    tuple(nearest_neighbor_algorithm_path), end_time_nearest
                    , exhaustive_algorithm_path_length, tuple(exhaustive_algorithm_path), end_time_exhaustive))

    # plot
    while True:
        n = int(input("\nEnter 1 to plot nearest neighbor\nEnter 2 to plot exhaustive(permutation)\nEnter 0 to exit\n"))
        if n == 0:
            break
        if n == 1:
            x = []
            y = []
            for j in range(len(nearest_neighbor_algorithm_path)):
                x.append(nearest_neighbor_algorithm_path[j][0])
                y.append(nearest_neighbor_algorithm_path[j][1])
            lines = plt.plot(x, y)
            plt.setp(lines, color='green', linewidth=2.0, linestyle='--', marker='o', markeredgecolor='blue',
                     markerfacecolor='blue')
            plt.plot(x[0], y[0], 'or')
            plt.show()

        if n == 2:
            x = []
            y = []
            for j in range(len(exhaustive_algorithm_path)):
                x.append(exhaustive_algorithm_path[j][0])
                y.append(exhaustive_algorithm_path[j][1])
            lines = plt.plot(x, y)
            plt.setp(lines, color='orange', linewidth=2.0, linestyle='--', marker='o', markeredgecolor='blue',
                     markerfacecolor='blue')
            plt.plot(x[0], y[0], 'or')
            plt.show()


run()
