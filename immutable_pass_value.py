# Explanation:
# try_update("inactive"): This function attempts to change user_status, but because user_status is an immutable string,
# the change only happens locally within the function. The global user_status remains "active".
#
# return_updated_status("banned"): This function doesn't directly modify the global variable. Instead, it returns the
# new value, which you can reassign to user_status. Now, the global user_status will be updated to "banned".
#

user_status = "active"


def try_update(new_status: str):
    user_status = new_status
    print(f"Inside function: {user_status}")


print(f"Before function call: {user_status}")
try_update("inactive")
print(f"After function call: {user_status}")


def return_updated_status(new_status: str):
    return new_status


user_status = return_updated_status("banned")
print(f"After function call: {user_status}")