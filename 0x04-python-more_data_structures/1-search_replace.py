def search_replace(my_list : list, search, replace):
    new_list = [replace if item == search else item for item in my_list]
    return new_list