def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a = len(s)
    if a%2==0:
        x= s[(a//2)-1]+s[(a//2)]
    else:
        x= s[(a//2)]
    return x
s = "aaaabraaaa"
print(main(s))