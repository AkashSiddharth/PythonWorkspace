import time

def timer(func):
    def wrapper(*args: list, **kargs: dict):
        start_time = time.time()
        # Executing the actual function here
        result = func(*args, **kargs)
        stop_time = time.time()
        print(f"Funtion {func.__name__!r} took: {stop_time - start_time:4f} secs")
        return result
    
    return wrapper

# Using the custom decorator
@timer # Equivalent to: sample_function = timer(sample_function)
def sample_function(n):
    return f"The Sum is {sum(range(n))}"


print(sample_function(123572890))