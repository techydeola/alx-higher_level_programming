def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for tupple in my_list:
        average += (tupple[0] * tupple[1])
        size += tupple[1]
    return (average / size)
