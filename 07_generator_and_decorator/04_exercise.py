# Caching Expensive Calculations

def cache_results(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return f"From Cache: {cache[args]}"
        
        result = func(*args)
        cache[args] = result
        return f"Computed: {result}"
    return wrapper
        
    

@cache_results
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(4,5))