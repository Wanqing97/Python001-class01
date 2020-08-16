import time,datetime
# # # 作业一：

# # # 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

# # 扁平序列：str
# # 容器序列：list、tuple、dict、collections.deque

# # 可变序列：list、dict、collections.deque
# # 不可变序列：tuple、str


# # # 作业二：
# # # 自定义一个 python 函数，实现 map() 函数的功能。

class map:
    
    def __init__(self,func,*args):
        self.iterators=args
        self.func=func
 
    def __iter__(self):
        return self.generator()
 
    def generator(self):
        iterators,func=self.iterators,self.func
        try:
            i = 0
            while 1:
                yield func(*[j[i] for j in iterators])
                i += 1
        except IndexError:
            pass

f=lambda x,y,z,w:x==y
a=[1,2,44,4,5,6,7,8,9]
b=[1,2,3,4,11,6,7,8,9]
print(list(map(f,a,b,a,b)))

# # # 作业三：
# # # 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
def timer(func):
    def inner2(*args,**kwargs):
        print(f'start')
        starttime = datetime.datetime.now()
        func(*args,**kwargs)
        endtime = datetime.datetime.now()
        print(f'running time：{endtime - starttime}')
    return inner2

@timer
def foo2(a, b):
    time.sleep(1)
    print(a + b)

foo2(50,10)