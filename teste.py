def myprint(*args):
    res=[]
    for x in args:
         res+=[str(x),]
    return ' '.join(res)

def myf():
    return  'myf called'

def square(x):
    return x*x
