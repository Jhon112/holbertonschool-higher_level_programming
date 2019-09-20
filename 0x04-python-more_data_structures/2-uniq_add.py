#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return (0)
    uniq = set(my_list)
    result = sum(map(lambda x: x, uniq))
    return (result)
