def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    z=0
    while i<len(s):

        if s[i].isalpha():

            z+=1
        i+=1

    return z
print(main('@com.uz#'))