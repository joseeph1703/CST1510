# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
# The error happens because 'status' is a local variable inside the function.
# It cannot be accessed outside, so we must return it.

    status = "OVER LIMIT" if value > limit else "OK"
    return status

print(check(87, 100))   # now works
