def tsp_greedy(name_file, distance_file):
    name_file = open(name_file)
    distance_file = open(distance_file)

    city_dict = {}
    city_counter = -1
    for city in name_file:
        city = city.strip()
        city_counter += 1
        city_dict[city_counter] = city

    distances_list = []
    for row in distance_file:
        row = row.split()
        distances_list.append(row)

        # turn strings into floats
        for list in distances_list:
            for str in range(len(list)):
                list[str] = float(list[str])

    # i = rows, j = columns
    i = 0
    j = -1
    final_distance_list = [0]
    for lst in distances_list:
        minimum = min(lst)
        for dist in lst:
            j += 1
            if dist == minimum:
                final_distance_list.append(j)


tsp_greedy("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/seven_cities_names.txt",
           "/Users/nathanielnowel/PycharmProjects/travellingsalesperson/seven_cities_distances.txt")
