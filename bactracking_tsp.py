def distance_between_two_cities(city1, city2, name_file, distance_file):
    name_file = open("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/seven_cities_names.txt")
    distance_file = open("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/seven_cities_distances.txt")

    distances_list = []
    for row in distance_file:
        row = row.split()
        distances_list.append(row)

        # turn strings into floats
        for lst in distances_list:
            for str in range(len(lst)):
                lst[str] = float(lst[str])

    location1 = city1
    location2 = city2

    distance = distances_list[location1][location2]
    return distance


def distance_calculator(list_of_cities, name_file, distance_file):
    current_city_dict = {}
    cityNum = 0
    for city in list_of_cities:
        current_city_dict[cityNum] = city
        cityNum += 1

    distance_list = []
    for cityNum in current_city_dict.keys():
        if cityNum < len(list_of_cities)-1:
            distance = distance_between_two_cities(current_city_dict[cityNum], current_city_dict[cityNum+1], name_file, distance_file)
            distance_list.append(distance)

    sum = 0
    for distance in distance_list:
        sum += distance

    return sum


def tsp_backtrack(name_file, distance_file):

    name_file = open(name_file)
    distance_file = open(distance_file)

    global city_names
    city_names = {}
    city_counter = -1
    for city in name_file:
        city = city.strip()
        city_counter += 1
        city_names[city_counter] = city

    global city_distances
    city_distances = []
    for row in distance_file:
        row = row.split()
        city_distances.append(row)

        # turn strings into floats
    for lst in city_distances:
        for str in range(len(lst)):
            lst[str] = float(lst[str])

    global best_tour
    best_tour = []

    for cityNum in city_names.keys():
        best_tour.append(cityNum)

    nonzero_cities = []
    for cityNum in city_names.keys():
        if cityNum != 0:
            nonzero_cities.append(cityNum)

    tsp_recursion([0], nonzero_cities, name_file, distance_file)

    final_city_list = []
    for cityNum in best_tour:
        final_city_list.append(city_names[cityNum])

    print(f"Distance: {distance_calculator(best_tour, name_file, distance_file)}")
    return final_city_list


def tsp_recursion(partial_tour, remaining_cities, name_file, distance_file):
    global best_tour

    if len(remaining_cities) == 0:
        if distance_calculator(partial_tour, name_file, distance_file) < distance_calculator(best_tour, name_file, distance_file):
            best_tour = partial_tour

    elif len(partial_tour) == 1:
        for i in range(len(remaining_cities)-1):
            if remaining_cities[i] < remaining_cities[i+1]:
                partial_tour_copy = partial_tour.copy()
                remaining_cities_copy = remaining_cities.copy()

                partial_tour_copy.append(remaining_cities[i])
                partial_tour_copy.append(remaining_cities[i+1])

                remaining_cities_copy.remove(remaining_cities[i])
                remaining_cities_copy.remove(remaining_cities[i+1])

                tsp_recursion(partial_tour_copy, remaining_cities_copy, name_file, distance_file)

    else:
        for city in remaining_cities:
            partial_tour_copy = partial_tour.copy()
            remaining_cities_copy = remaining_cities.copy()

            partial_tour_copy.insert(-2, city)
            remaining_cities_copy.remove(city)

            tsp_recursion(partial_tour_copy, remaining_cities_copy, name_file, distance_file)


print(tsp_backtrack("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/seven_cities_names.txt",
                    "/Users/nathanielnowel/PycharmProjects/travellingsalesperson/seven_cities_distances.txt"))