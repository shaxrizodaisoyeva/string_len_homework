def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    a = int(num1)+int(num2)
    a =str(a)
    return a 
num1 ="2"
num2 = "5"
print(main(num1,num2))