def expressions_matter(a: int, b: int, c: int) -> int:
    """
    Given three integers a, b, c return the largest number obtained after inserting the following
    operators and brackets: +, *, ()
    :param a:
    :param b:
    :param c:
    :return: max value obtained from every combination of a,b,c with [*+()]
    """
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))
