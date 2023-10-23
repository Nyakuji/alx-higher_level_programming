#!/usr/bin/python3
"""
    prints x elements of a list.

    """


def safe_print_list(my_list=[], x=0):
    count = 0
    for x in range(0, x):
        try:
            print(my_list[x], end="")
            count += 1
        except (IndexError, TypeError):
            break
    print("")
    return(count)
