def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

# # Example 2:
# ft_filter(lambda dum: not (dum % 2), x)
# # Output:
# <generator object ft_filter at 0x7f709c777d00> # The adress will be different
# list(ft_filter(lambda dum: not (dum % 2), x))
# # Output:
# [2, 4]