# Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You are about to call {func.__name__}{args}")
        return print(f"It returned: {func(*args, **kwargs)}")
    return wrapper

# Use the decorator 👇


@logging_decorator
def multiply(x, y, z):
    return x * y * z


multiply(2, 3, 4)
