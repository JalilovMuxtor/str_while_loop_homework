def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    y=0
    while i<len(s):

        if s[i].isalpha():
            
            y+=1
        i+=1
    return y
print(main('python 2022'))