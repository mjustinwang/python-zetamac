from typing import Literal


def problem_gen(digits: int, op_type: Literal["+", "-", "/", "*"]) -> tuple[str, int]:
    """Generates a random arithmetic problem.

    Args:
        digits: Determines the digits of the number of the problem.
        op_type: Determines the operation of the arithmetic problem.

    Returns:
        A tuple where the first elements is the equation as a string, and the second element is the answer as a integer.

    Examples:
        >>> problem_gen(digits=2, op_type="+") 
        ()
    """

    pass


