#decorators in python
def greet (fx):
    def mfx(*args , **kwargs):
        print("good morning")
        fx(*args , **kwargs)
        print("thanks for using this function.")
    return mfx

@greet
def hello():
    print("hello world")
# decorator doesnt support arguments unless modified with *args and **kwargs
@greet
def add ():  #(a,b) wont work 
    a = 1
    b = 34
    print(a+b)
hello()
add()
# greet(hello()) also works

@greet
def add2(a,b):
    print(a+b)

add2(4,7)
