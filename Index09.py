def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    
    if type(s) == str:
        return -1
    else:
        return int(s)
    
print(main('7'))