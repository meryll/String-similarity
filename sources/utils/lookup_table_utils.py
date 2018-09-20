def create_id_lookup_table(array):
    look_up = {}
    index = 1

    for value in array:
        look_up[value] = index
        index += 1

    return look_up
