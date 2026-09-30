import time
import random as r
import sys
from generator import problem_gen

def run_game() -> None:
    """Runs the main game loop.

    Asks the user for: max digits, allowed operations ("+", "-", "*", "/"), total allowed time.

    Generates question and prompts the user for answers while timer runs and increments the timer.

    Keeps track of score and prints the results in the terminal.
    
    """

    settings = get_user_settings()

    max_digits = settings["max_digits"]
    allowed_ops = settings["allowed_ops"]
    total_time = settings["total_time"]

    score = 0
    time_spent = []

    # Game loop that generates questions
    while True:
        print(f"TOTAL TIME LEFT: {total_time}")
        start = time.time()

        problem = problem_gen(digits=max_digits, op_type=r.choice(allowed_ops))

        equation, ans = problem

        # Internal loop that handles guesses per question
        while True:
            guess = get_user_ans(equation=equation)

            if guess == ans:
                end = time.time()
                time_diff = end - start

                time_spent.append(round(time_diff, 1))

                total_time = round(total_time - time_diff, 1)

                if total_time <= 0:
                    end_game(score=score, time_spent=time_spent)
                else:
                    score += 1
                    break





def get_user_settings() -> dict:
    """Prompts the user for quiz configuration settings and handles input validation.

        Prompts for:
            - Maximum digits per number
            - Allowed math operations ("+", "-", "*", "/")
            - Total allowed time in seconds

        Returns:
            dict: A dictionary containing:
                - "max_digits" (int): Maximum digit length for numbers.
                - "allowed_ops" (list[str]): Operators included in the quiz.
                - "total_time" (int): Time limit in seconds.

        Examples:
            >>> get_user_settings()
            {'max_digits': 2, 'allowed_ops': ['+', '*'], 'total_time': 100}
            >>> get_user_settings()
    """
    max_digits = get_int("Max digits per number: ")
    allowed_ops = []

    for s in ['+', '-', '*', '/']:
        user_input = input(f"Do you want this operation: \"{s}\"? y/n: ")
        if user_input == "y":
            allowed_ops.append(s)

    total_time = get_int("Total time in sec: ")

    return {
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

def end_game(score: int, time_spent: list[float]):
    """Takes game stats and ends the game while printing out the stats nicely
    """
    # Handle the case where the player ran out of time before answering any questions
    if not time_spent:
        avg_time = 0.0
        best_time = 0.0
    else:
        avg_time = round(sum(time_spent) / len(time_spent), 2)
        best_time = min(time_spent)

    banner = "=" * 45
    divider = "-" * 45

    message = f"""
{banner}
              ⏰ TIME'S UP! ⏰
{banner}
  GREAT JOB! HERE IS YOUR PERFORMANCE SUMMARY:

  • Total Correct Answers : {score}
  • Average Speed         : {avg_time} sec / question
  • Fastest Answer        : {best_time} sec
{divider}
  Thanks for playing! Keep practicing!
{banner}
"""
    sys.exit(message)

def get_int(prompt: str) -> int:
    """Asks user for input and validates if input is an integer.

    Args:
        prompt: The message shown to the user.
    
    Returns:
        Validated integers.
    """
    
    #Loop thats only ends if user_input is an integer or exits the whole program by EOF
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            continue
        except EOFError:
            sys.exit("Thanks")

    
