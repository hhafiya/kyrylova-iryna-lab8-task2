"""
Program retuns bool statement after checking whether a column,
row or block has the same numbers.
link: https://github.com/hhafiya/kyrylova-iryna-lab8-task2.git
"""
def is_different(case: str) -> bool:
    """
    Function chechs whether it has the same numbers in string.
    Returns False or True
    >>> is_different(" 6  83  *")
    True
    >>> is_different("**3 3****")
    False
    """
    numbers = []
    for i in case:
        if i.isdigit():
            numbers.append(i)
    return len(numbers) == len(set(numbers))
