def authenticate(function):
    def wrapper(*args, **kwargs):
        is_authenticated = True
        if is_authenticated:
            result = function(*args, **kwargs)
            print("Access granted.")
            return result
        else:
            print("Access denied.")
    return wrapper


@authenticate
def private_function():
    print("This is a private function.")


@authenticate
def a_function(*args):
    return sum(args)


print(a_function(1, 2, 3))
