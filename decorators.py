
# zadanie 1 stwórz funkcję, która będzie liczyła czas wykonywania zadania
# import time

# def count_execution_time(func):
#     def wrapper(*args,**kwargs):
#         start = time.perf_counter()
#         result=func(*args,**kwargs)
#         end=time.perf_counter()
#         total_time = end - start
#         return (f"Function {func.__name__} has been executed in {total_time} secounds")
#     return wrapper
    
# @count_execution_time
# def loop():
#     return list(a**2 for a in range(20000000))
    
# print(loop())


# Napisz dekorator dla funkcji, który będzie logował informacje o każdym wywołaniu funkcji, takie jak nazwa funkcji, przekazane argumenty i zwrócony wynik. Informacje te powinny być zapisywane do pliku lub wyświetlane na konsoli.

def log_function_call(func):
    def wrapper(*args,**kwargs):
        print(f"Function '{func.__name__}' has been called with arguments:")
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned result: {result}")
        return result
    return wrapper

@log_function_call
def example_function(a,b,c):
    return a*b*c

result = example_function(1,2,3)
# print("Result of example function:", result)