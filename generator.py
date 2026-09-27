from typing import Literal
import random as r

def problem_gen(digits: int, op_type: Literal["+", "-", "/", "*"]) -> tuple[str, int]:
    """Generates a random arithmetic problem.

    Args:
        digits: Determines the digits of the number of the problem.
        op_type: Determines the operation of the arithmetic problem.

    Returns:
        A tuple where the first elements is the equation as a string, and the second element is the answer as a integer.

    Examples:
        >>> problem_gen(digits=2, op_type="+") 
        (13 + 5 = , 18)
        >>> problem_gen(digits=3, op_type="*")
        (199 * 799, 159001)
        >>> problem_gen(digits=2, op_type="/)
        (40 / 5 = , 8)
    """
    if op_type in ["+", "-", "*"]:
        #generates random numbers depending on the maximum allowed of digits of a number.
        x = r.randint(1, 10**digits - 1)
        y = r.randint(1, 10**digits - 1)

        #Creating the second element of the tuple, the answer.
        if op_type == "+":
            answer = x + y
        elif op_type == "-":
            answer = x - y
        elif op_type == "*":
            answer = x * y

        #return the equation and the answer in the form of a tuple.
        return (f"{x} {op_type} {y} = ", answer)

    elif op_type == "/":
        #generates random numbers depending on the maximum allowed of digits of a number.
        answer = r.randint(1, 10**digits - 1)
        division = r.randint(1, 10**digits - 1)
        
        #we need to make sure that the answer of the equation is an integer.
        #Let's split up the equation into number_1 and division and answer.
        #So if we have 1200 / 20 = 60, number_1 = 1200, division = 20 and answer = 60.
        #to make sure the answer is always an integer,
        #we need to make number_1 = answer * division.
        number_1 = answer * division
        
        #return the equation and the answer in the form of a tuple
        return (f"{number_1} {op_type} {division} = ", answer)


