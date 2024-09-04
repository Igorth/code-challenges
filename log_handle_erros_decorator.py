from datetime import datetime


def log_and_handle_errors(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"[{start_time}] Starting function '{function.__name__}' with arguments: {args} {kwargs}")
        try:
            result = function(*args, **kwargs)
            end_time = datetime.now()
            print(f"[{end_time}] End function '{function.__name__}' completed successfully")
            return result
        except Exception as e:
            error_time = datetime.now()
            print(f"[{error_time}] Error occurred in function '{function.__name__}': {e}")
            return "An error occurred. Please try again"
    return wrapper


@log_and_handle_errors
def divide_numbers(a, b):
    return a / b


print(divide_numbers(5, 5))
