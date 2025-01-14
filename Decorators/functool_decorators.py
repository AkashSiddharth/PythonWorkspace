import functools

# Simple implementation
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Cache implementation
def cache_fibonacci(n, cache = {}):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1    
    
    cache[n] =  cache_fibonacci(n - 1, cache) + cache_fibonacci(n - 2, cache)
    return cache[n]

# Decorator Cache
@functools.cache
def cfibonacci(n):
    if n < 2:
        return n
    else:
        return cfibonacci(n - 1) + cfibonacci(n - 2)

print(fibonacci(40))
print(cache_fibonacci(40))
print(cfibonacci(40))
