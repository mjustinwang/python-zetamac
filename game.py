import time
import random as r
import sys
#from generator import problem_gen

def run_game() -> None:
    """Runs the main game loop.

    Asks the user for: # of questions, max digits, allowed operations ("+", "-", "*", "/"),
    total allowed time.

    Generates question and prompts the user for answers while timer runs and increments the timer.

    Keeps track of score and prints the results in the terminal.
    
    """

    settings = get_user_settings()

    num_questions = settings["num_questions"]
    max_digits = settings["max_digits"]
    allowed_ops = settings["allowed_ops"]
    total_time = settings["total_time"]

    while total_time > 0:
        start = time.time()

        #problem = problem_gen(digits=max_digits, op_type=r.choice(allowed_ops))
        problem = ("45 + 32 =", 77)

        equation, ans = problem

        ans = get_user_ans(equation=equation)


        print(ans)



def get_user_settings() -> dict:
    """Prompts the user for quiz configuration settings and handles input validation.

        Prompts for:
            - Number of questions
            - Maximum digits per number
            - Allowed math operations ("+", "-", "*", "/")
            - Total allowed time in seconds

        Returns:
            dict: A dictionary containing:
                - "num_questions" (int): Total questions for the quiz.
                - "max_digits" (int): Maximum digit length for numbers.
                - "allowed_ops" (list[str]): Operators included in the quiz.
                - "total_time" (int): Time limit in seconds.

        Examples:
            >>> get_user_settings()
            {'num_questions': 5, 'max_digits': 2, 'allowed_ops': ['+', '*'], 'total_time': 100}
            >>> get_user_settings()
    """

    num_questions = int(input("Number of questions: "))
    max_digits = int(input("Max digits per number: "))
    allowed_ops = []

    for s in ['+', '-', '*', '/']:
        user_input = input(f"Do you want this operation: \"{s}\"? y/n: ")
        if user_input == "y":
            allowed_ops.append(s)

    total_time = int(input("Total time in sec: "))

    return {
        "num_questions": num_questions,
        "max_digits": max_digits,
        "allowed_ops": allowed_ops,
        "total_time": total_time
    }
    

def get_user_ans(equation: str) -> int:
    """Validates user input for valid answer.

    Args:
        equation: The equation with which the user gets prompt
    
    Returns:
        The user answer as an integer
    """

    while True:
        try:
            ans = int(input(f"{equation} "))
            return ans
        
        except ValueError:
            # Only catch value errors (like typing letters), not KeyboardInterrupt
            pass
        except (KeyboardInterrupt, EOFError):
            # Gracefully exit on Ctrl+C
            sys.exit("\nProgram stopped.")

run_game()