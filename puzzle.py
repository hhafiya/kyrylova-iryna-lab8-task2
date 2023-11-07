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
def validate_board(board: list) -> bool:
    """
    Function checks whether it has the same numbers 
    in one line, column or block.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", \
"* 4 1****", "     9 5 ", " 6  83  *", \
"3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", \
"* 4 1****", "     9 5 ", " 6  83  *", \
"3   7  **", "  8  2***", "  2  ****"])
    True
    """
    for row in board:
        if not is_different(row):
            return False
    for column in range(9):
        col = ''.join([board[row][column] for row in range(9)])
        if not is_different(col):
            return False
    col_list = []
    row_list = []
    block_list_1 = []
    for column in range(9):
        col = ''.join([board[row][column] for row in range(9)])
        col_list.append(col)
    for row in board:
        row_list.append(row)