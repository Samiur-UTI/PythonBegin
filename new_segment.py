def my_decorator (func):
    def wrapper (n,g):
        print(f'this message is from {n}')
        func(n,g)
        print(f'Everyone please apprciate {n}s {g}')
    return wrapper
@my_decorator
def hello_world(name,greeting):
    print(f'{name} says {greeting}')
    
hello_world('Sami','Hellloooo')