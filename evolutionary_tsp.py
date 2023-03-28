import random


def distance_between_two_cities(city1, city2, name_file, distance_file):
    name_file = open("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/thirty_cities_names.txt")
    distance_file = open("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/thirty_cities_distances.txt")

    city_dict = {}
    city_counter = -1
    for city in name_file:
        city = city.strip()
        city_counter += 1
        city_dict[city] = city_counter

    distances_list = []
    for row in distance_file:
        row = row.split()
        distances_list.append(row)

        # turn strings into floats
        for lst in distances_list:
            for str in range(len(lst)):
                lst[str] = float(lst[str])

    location1 = city_dict[city1]
    location2 = city_dict[city2]

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


def tsp_mutation(name_file, distance_file):
    name_file = open(name_file)
    distance_file = open(distance_file)

    city_list = []
    for city in name_file:
        city = city.strip()
        city_list.append(city)

    distances_list = []
    for row in distance_file:
        row = row.split()
        distances_list.append(row)

        # turn strings into floats
        for lst in distances_list:
            for str in range(len(lst)):
                lst[str] = float(lst[str])

    final_distance_list = []
    final_location_list = [0]
    current_city_list = []

    # initial minimum
    minimum = sum(distances_list[0])

    # initialize
    for city in city_list:
        current_city_list.append(city)
    current_city_list_copy = current_city_list.copy()

    # mutate
    best_tours = []
    while len(best_tours) < 5:

        improvement = False

        for offspring in range(10):

            current_city_list_copy = current_city_list.copy()
            city_to_remove = random.choice(current_city_list_copy)
            current_city_list_copy.remove(city_to_remove)

            city_to_add = random.choice(range(len(current_city_list)))
            current_city_list_copy.insert(city_to_add, city_to_remove)

            # select
            if distance_calculator(current_city_list_copy, name_file, distance_file) <= minimum:
                improvement = True
                minimum = distance_calculator(current_city_list_copy, name_file, distance_file)
                current_city_list = current_city_list_copy

        # terminate
        if not improvement:
            best_tours.append(current_city_list)
            # MUTATE current_city_list THREE TIMES
            for mutation in range(3):
                city_to_add = random.choice(range(len(current_city_list)))
                city_to_remove = random.choice(current_city_list)
                current_city_list.remove(city_to_remove)
                current_city_list.insert(city_to_add, city_to_remove)
            # set mutated version to be new parent
            current_city_list = current_city_list

    total_distance_list = []
    for tour in best_tours:
        total_distance = distance_calculator(tour, name_file, distance_file)
        total_distance_list.append(total_distance)

    location = 0
    minimum_distance = min(total_distance_list)
    for distance in total_distance_list:
        if total_distance_list[location] == minimum_distance:
            best_tour_location = location
        location += 1

    print(f"Distance: {total_distance_list[best_tour_location]}")
    best_tour = best_tours[best_tour_location]

    return best_tour


print(tsp_mutation("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/thirty_cities_names.txt",
                   "/Users/nathanielnowel/PycharmProjects/travellingsalesperson/thirty_cities_distances.txt"))

