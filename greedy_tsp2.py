import random
def tsp_greedy(name_file, distance_file):
    # Parse the distance file and store the distances in a 2D array
    with open(distance_file, 'r') as f:
        distances = [[float(d) for d in line.split()] for line in f.readlines()]

    # Parse the name file and store the city names in a list
    with open(name_file, 'r') as f:
        cities = [line.strip() for line in f.readlines()]

    # Start with the first city in the list
    start_city = random.randint(0, len(cities)-1)
    current_city = start_city
    print(f'abc: {current_city}')
    visited_cities = [current_city]
    tour_distance = 0

    # Find the nearest neighbor until all cities have been visited
    while len(visited_cities) < len(cities):
        nearest_neighbor = None
        nearest_distance = float('inf')
        for neighbor_city in range(len(cities)):
            if neighbor_city not in visited_cities and distances[current_city][neighbor_city] < nearest_distance:
                nearest_neighbor = neighbor_city
                nearest_distance = distances[current_city][neighbor_city]
        if nearest_neighbor is None:
            # If there is no unvisited neighbor, return to the starting city
            nearest_neighbor = start_city
            tour_distance += distances[current_city][nearest_neighbor]
        visited_cities.append(nearest_neighbor)
        tour_distance += nearest_distance
        current_city = nearest_neighbor

    # Return to the starting city to complete the tour
    tour_distance += distances[current_city][start_city]
    visited_cities.append(start_city)

    # Convert the list of city indices to a list of city names
    tour = [cities[i] for i in visited_cities]

    return tour, tour_distance


# example usage
tour, tour_distance = tsp_greedy('thirty_cities_names.txt', 'thirty_cities_dist.txt')
print(f"Tour: {tour}")
print(f"Tour distance: {tour_distance}")

