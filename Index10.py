def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    ans = 0
    if type(int(s[0])) == int:
        ans += int(s[0])
    if type(int(s[1])) == int:
        ans += int(s[1])
    if type(int(s[2])) == int:
        ans += int(s[2])
    if type(int(s[3])) == int:
        ans += int(s[3])
    if type(int(s[4])) == int:
        ans += int(s[4])
    return ans