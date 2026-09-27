def run_game() -> None:
    """Runs the main game loop.

    Asks the user for: # of questions, max digits, allowed operations ("+", "-", "*", "/"),
    total allowed time.

    Generates question and prompts the user for answers while timer runs and increments the timer.

    Keeps track of score and prints the results in the terminal.
    
    """

    pass



def get_user_settings():
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
            {'num_questions': 10, 'max_digits': 3, 'allowed_ops': ['-', '/'], 'total_time': 200}
            >>> get_user_settings()
            {'num_questions': 15, 'max_digits': 1, 'allowed_ops': ['+', '-', '*', '/'], 'total_time': 300}
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
    

def game_timer(sec: int):
    """Starts the game timer.

    Gets incremented as time goes on while the problems are being asked.

    Args:
        sec: duration of the timer in second.
    """
    pass


get_user_settings()