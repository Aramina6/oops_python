#Simple Logging Decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
# Output:
# Calling function: add_numbers
# 5




#Timing Decorator
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

@measure_time
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

fibonacci(35)
# Output:
# Function fibonacci took 0.592375 seconds to execute.




#Parameter Validation Decorator
  def validate_parameters(func):
    def wrapper(a, b):
        if not isinstance(a, (int, float)):
            raise TypeError("a must be a number")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be a number")
        return func(a, b)
    return wrapper

@validate_parameters
def divide(a, b):
    return a / b

result = divide(10, 2)
print(result)  # Output: 5.0

result = divide(10, "2")
# TypeError: b must be a number



#Caching Decorator
def cache_result(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cache_result
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

print(fibonacci(35))  # First call takes time, subsequent calls are fast
print(fibonacci(35))  # Output: result from cache
