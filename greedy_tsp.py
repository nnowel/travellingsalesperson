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
        for lst in distances_list:
            for str in range(len(lst)):
                lst[str] = float(lst[str])

    row = 0
    column = -1
    final_distance_list = []
    final_location_list = [0]

    # current_city = 0

    for lst in range(len(distances_list) - 1):  # loop until you add the correct number of cities
        minimum = max(distances_list[row])  # initial minimum value
        for distance in distances_list[row]:

            # for next_city in range(len(distances_list[current_city])):

            column += 1

            # print(distance)
            # print(minimum)
            # print(row)
            # print(column)
            # print()

            if 0 < distance <= minimum and column not in final_location_list:  # ensures same city is not added twice
                # store local min information
                minimum = distance
                location = column

                # print(f"minimum: {minimum}")
                # print(f"location: {location}")
                # print()

            if column == len(distances_list[row]) - 1:
                # once all distances have been looped through, the local min is now the absolute min
                final_location_list.append(location)
                final_distance_list.append(minimum)
                row = location
                column = -1

    # print(final_location_list)
    # print(final_distance_list)

    distance_sum = 0
    for distance in final_distance_list:
        distance_sum += distance

    print(f"Total Distance: {distance_sum}")

    final_city_list = []
    for city in final_location_list:
        final_city_list.append(city_dict[city])

    return final_city_list


print(tsp_greedy("/Users/nathanielnowel/PycharmProjects/travellingsalesperson/thirty_cities_names.txt",
                 "/Users/nathanielnowel/PycharmProjects/travellingsalesperson/thirty_cities_distances.txt"))
