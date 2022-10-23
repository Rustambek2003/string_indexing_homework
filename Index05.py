def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    ans = 0
    if type(int(s[0])) == int:
        ans += 1
    if type(int(s[0])) == int:
        ans += 1
    if type(int(s[0])) == int:
        ans += 1
    if type(int(s[0])) == int:
        ans += 1
    if type(int(s[0])) == int:
        ans += 1
    return ans
print(main("32x3z"))