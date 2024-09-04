from datetime import datetime


def log_execution_time(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = function(*args, **kwargs)  # b_function(5, 10)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Function name: {function.__name__} Execution time: {execution_time}")
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function


@log_execution_time
def a_function():
    print("This is a sample function")


@log_execution_time
def b_function(a, b):
    return a * b


@log_execution_time
def c_function(c, d):
    return c + d


a_function()
b_function(5, 10)
c_function(5, 4)
