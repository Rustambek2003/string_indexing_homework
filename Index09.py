def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if type(int(s)) == int:
        return int(s)
    elif type(str(s)) == str:
        return -1
print(main('k'))