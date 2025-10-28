from curses import flash
from email import iterators
from typing import Iterator


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    valid:False
    if isinstance(iterable, list) == True:
        valid = True
    if isinstance(iterable, tuple) == True:
        valid = True
    if isinstance(iterable, Iterator) == True:
        valid = True

    if valid == False:
        raise Exception("ERROR")
    
    res:list = []

    res.append(function_to_apply(elt) for elt in iterable)
    return res


# Example 1:
x = [1, 2, 3, 4, 5]
ft_map(lambda dum: dum + 1, x)
# Output:
# <generator object ft_map at 0x7f708faab7b0> # The adress will be different

res = ft_map(lambda t: t + 1, x)
print(res)
print(list(res))
# Output:
# [2, 3, 4, 5, 6]