def tsp_greedy(name_file, distance_file):
    name_file = open(name_file)
    distance_file = open(distance_file)

    path = ''
    city_num = 0
    for city_name in name_file:
        city_num += 1
        city_name = city_num
