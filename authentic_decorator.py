user_session = {
    "is_authenticated": False,
    "user_id": None,
    "username": None
}


def authenticate(function):
    def wrapper(*args, **kwargs):
        # Check if user is authenticated by inspecting the session data
        if user_session['is_authenticated']:
            print("Access granted")
            return function(*args, **kwargs)  # Call the original function
        else:
            print("Access denied. Please log in.")
            return None  # Return None to indicate access denied
    return wrapper


@authenticate
def private_access():
    return "This is a sensitive data."


print(private_access())

user_session["is_authenticated"] = True
user_session["user_id"] = 1
user_session["username"] = "john_doe"


print(private_access())
