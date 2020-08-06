from curses import wrapper




def wrapper(fun):
    def hello(*args, **kwargs):
        print("hello")
        fun()
        print("good bye")
    return hello

def tex1():
    print('song')
    print('tex1')

@wrapper
def tex2():
    print('dong')
    print('tex2')



def test_case():
    tex2()

