def greet(name):
    return "Hello " + name

def call_func(func):
    other_name = "Saurabh"
    return func(other_name)

print(call_func(greet))

# Outputs: Hello Saurabh
