def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    x= "["
    if len(s1)%2==1:
        x += s1
    if len(s2)%2==1:
        x += ", "+s2
    if len(s3)%2==1:
        x += ", "+s3
    return x+ "]"
s1 = "abicd"
s2 = "efpjlplk"
s3 = "azilz"
print(main(s1,s2,s3))