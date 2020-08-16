学习笔记
Python高阶语法：
一、变量赋值
	# 问题1: a、b、c三个id是否相同
	a = 123
	b = 123
	c = a
	print(id(a))
	print(id(b))
	print(id(c))
	a=b=c
	
	#############
	# 问题2: a、b、c的值分别是多少
	a = 456
	print(id(a))
	c = 789
	c = b = a     #b和c都等于a
	a=b=c=456
	
	#############
	# 问题3: x、y的值分别是什么
	x = [1,2,3]
	y = x
	x.append(4)
	print(x)   [1,2,3,4]
	print(y)   [1,2,3,4]
	
	#############
	# 问题4: a、b的值分别是多少
	a = [1, 2, 3]
	b = a
	a = [4, 5, 6]
	print(a)   [4,5,6]
	print(b)   [1,2,3]
	
	
	#############
	# 问题5: a、b的值分别是多少
	a = [1, 2, 3]
	b = a
	a[0],a[1],a[2] = 4, 5, 6
	print(a)   [4,5,6]
	print(b)   [4,5,6]
	注意问题4和问题5结果不一样
	
	• 可变数据类型： 
        • 列表list 
        • 字典dict
		缺点：地址不会变，内容发生变化
	• 不可变数据类型（对象的本身）： 
        • 整型int 
        • 浮点型float 
        • 字符串型string 
        • 元组tuple
		优点：考虑性能问题，不可变数据类型引用的是相同对象，只占一块内存。
		缺点，需要对变量进行运算，必须新创建一个对象。不使用的话会被自动回收
二、序列
	1.序列分类：
		○ 容器序列：list、tuple、collections.deque等，能存放不同类型的数据
		○ 扁平序列：str、bytes、bytearray、memoryview（内存视图）、array.array等，存放的是类型的数据，扁平序列只能容纳一种类型
	
	2.只有容器序列存在深拷贝、浅拷贝的问题
		注意：非容器（数字、字符串、元组）类型没有拷贝问题
		
		import copy
		copy.copy(object)  
		copy.deepcopy(object)    把值全部拷出来并申请一段内存放在里面
	
		# 容器序列的拷贝问题
		old_list = [ i for i in range(1, 11)]
		new_list1 = old_list
		new_list2 = list(old_list)
		#1和2并不是同一个列表
		
		# 切片操作，依然会创建一个全新的列表
		new_list3 = old_list[:]
		
		# 嵌套对象，list1也随之改变，其他不变
		old_list.append([11, 12])

三、字典与扩展内置数据类型
	可使用collections标准库来扩展内置数据类型
	
	常用三个方法：
		○ namedtuple 带命名的元组
		○ deque 双向队列
		○ counter 计数器
	
	
	from collections import namedtuple
	Point = namedtuple('Ponit', ['x','y'])
	p = Point(11, y=22)
	print(p[0] + p[1])
	x, y = p
	print(p.x + p.y)
	print(p)
	

四、函数
函数需要掌握四个部分：
	• 调用
	• 作用域
	• 对参数的处理
	• 返回值

1.函数的调用
	func,类名        传递函数的对象
	func()，类()    传递函数的返回值
2.变量的作用域（命名空间）
	A.高级语言对变量的使用：
		○ 变量声明
		○ 定义类型（分配内存空间大小）
		○ 初始化（赋值、填充内存）
		○ 引用（通过对象名称调用对象内存数据）
	
	python和高级语言有很大的差别，在模块、类和函数中才会有作用域
	
	B.python作用域遵循LEGB规则
	LEGB（需要清楚地认识每个字母对应的每一部分）：
		○ Local：函数内的名字空间
		○ Enclosing function locals：外部嵌套函数的名字空间（例如closure）
		○ Global：函数定义所在模块（文件）的名字空间
		○ Builtin（Python）：Python内置模块的名字空间
	
		x = 'Global'
		def func2():
		    x = 'Enclosing'
		    def func3():
		        x = 'Local'
		        print (x)
		    func3()
	
	
	C.LEGB主要解决两大问题：
		○ 同名不同作用域
		○ 查找顺序问题
		# prog1  同名不同作用域问题
		x = 1 
		def func():
		    x = 2
		func()
		print (x)   #1 
		
		# prog2 查找顺序问题（函数内部没有参数，会向上查找）
		y = 2
		def func2():
		    print(y)
		func2()   #2
		
		# prog3  error
		def func3():
		    z = 3
		func3()
		print(z)   #z is not defined
		
		# prog4 error
		def func4():
		    print(a)
		func4()
		a = 100     #顺序问题 a is not defined
        
3.函数的可变长参数（必须掌握）
	A.def func(*args, **kargs):
		*args 实质就是将函数传入的参数，存储在元组类型的变量args当中；
		执行顺序是先找**kargs，没有匹配的成为*args
	
	B.偏函数: 存储用户不需要关心的参数
		functools.partial：返回一个可调用的partial对象
		使用方法：partial(func,*args,**kw)
		注意！
			§ func必须是参数
			§ 至少需要一个args或kw参数
			
4.高阶函数与lambda表达式区别
Lambda表达式（匿名函数）
	k = lambda  x:x+1
	print(k(1))

	Lambda表达式后面只能有一个表达式，不是所有的函数逻辑都能封装进去
		○ 实现简单函数的时候可以使用Lambda表达进行替代
		○ 使用高阶函数的时候一般使用Lambda表达式

高阶函数：
	高阶：参数是函数、返回值是函数
	常见的高阶函数：map、reduce、filter、apply
	apply在Python2.3被移除，reduce被放在functools包中
	推导式和生成器表达式可以替代map和filter函数
	
	map映射，square一定是可执行对象，后面的值依次对前面的对象进行处理，工作方式是迭代器
	
	重点看官方文档functools和itertools

5.返回值
返回的关键字：return、yield
返回的对象：可调用对象--闭包（装饰器）

	闭包的好处：
		a.外部的函数和内部的函数不相关，外部函数初次定义固定某些变量的值
		b.定义态：设置的模式是在函数定义的时候就设置好了，而不是运行时再设置规则
	
		nonlocal访问外部函数的局部变量
		
6.装饰器
好处：
	• 增强而不改变原有函数
	• 装饰器强调函数的定义态而不是运行态

语法糖的展开：
	@decorate
	def target():
		print('do something')
	
被装饰函数(3种)
	带参数，带不定长参数，带返回值
	A.# 被修饰函数带参数
	def outer(func):
	    def inner(a,b):
	        print(f'inner: {func.__name__}')
	        print(a,b)
	        func(a,b)
	    return inner
	@outer
	def foo(a,b):
	    print(a+b)
	    print(f'foo: {foo.__name__}')
	    
	    
	foo(1,2)   
		#inner: foo
		#1 2
		#3
		foo: inner
	foo.__name__    #inner
	############################################
	B.# 被修饰函数带不定长参数
	
	def outer2(func):
	    def inner2(*args,**kwargs):
	        func(*args,**kwargs)
	    return inner2
	@outer2
	def foo2(a,b,c):
	    print(a+b+c)
	    
	foo2(1,3,5)   #9
	
	############################################
	C.# 被修饰函数带返回值
	def outer3(func):
	    def inner3(*args,**kwargs):
	        ###
	        ret = func(*args,**kwargs)
	        ###
	        return ret
	    return inner3
	@outer3
	def foo3(a,b,c):
	    return (a+b+c)
	    
	print(foo3(1,3,5))     #9

装饰器堆叠 注意 顺序问题

Python内置装饰器：常用两个：wraps, lru_cache. 都在functools库里
	A. # functools.wraps
	# @wraps接受一个函数来进行装饰
	# 并加入了复制函数名称、注释文档、参数列表等等的功能
	# 在装饰器里面可以访问在装饰之前的函数的属性
	不改变内部函数的名字
	
	B. # functools.lru_cache
	# 《fluent python》的例子
	# functools.lru_cache(maxsize=128, typed=False)有两个可选参数
	# maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放
	# typed若为True，则会把不同的参数类型得到的结果分开保存
	
五、对象协议与鸭子类型
	用魔术方法实现对象协议
	分类：
		1.容器类型协议：
			__str__ 打印对象时，默认输出该方法的返回值
			__getitem__、__setitem__、__delitem__ 字典索引操作
			__iter__ 迭代器
			__call__ 可调用对象协议
			
		2.比较大小的协议
			__eq__  等于
			__gt__ 大于
			
		3.描述符协议和属性交互协议
		__get__
		__set__
		
		4.可哈希对象
		__hash__
		
	
	上下文管理器
		with上下文表达式的用法
		使用__enter__()   __exit__()实现上下文管理器

六、返回值另一重要的表达式yield

生成器
	1.在函数中使用yield关键字，可以实现生成器
	2。生成器可以让函数返回可迭代对象
	3.yield和return不同，return返回后，函数状态终止，yield保持函数的执行状态，返回后，函数回到之前保存的状态继续执行
	4.函数会被yield暂停，局部变量也会被保存
	5.迭代器终止时，会抛出StopIteration异常
	
	def func():
		yield 0
	
	type(func())           #<class 'generator'>
	
	[i for i in range(0,11)]
	(i for i in range(0,11))     #generator
	
	Iterables：包含__getitem__() 或 __iter__()方法的容器对象    可迭代
	Iterator：包含next() 和 __iter__()方法
	generator： 包含yield语句的函数
	
	Iterables 包含 iterator 包含 generator
	
	# 结论一  列表是可迭代对象，或称作可迭代（iterable）,
	#         不是迭代器（iterator）
	# __iter__方法是 iter() 函数所对应的魔法方法，
	# __next__方法是 next() 函数所对应的魔法方法
	# 结论二 生成器实现完整的迭代器协议
	# 只要一个函数的定义中出现了 yield 关键词，则此函数将不再是一个函数，
	# 而成为一个“生成器构造函数”，调用此构造函数即可产生一个生成器对象。
	# 结论三： 有yield的函数是迭代器，执行yield语句之后才变成生成器构造函数
	
		hasattr可检测是否是迭代器
	
	# itertools的三个常见无限迭代器
	1.itertools.count()  # 计数器 
	    next(count)
	2.itertools.cycle( ('yes', 'no') ) # 循环遍历
	3.itertools.repeat(10, times=2)  # 重复
	
	迭代器使用的注意事项：
	1.# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效
	# 尾插入操作不会损坏指向当前元素的List迭代器,列表会自动变长
	2.# 迭代器一旦耗尽，永久损坏
	
	yield表达式：
	# next() 或者 send(None) 会让yield的暂停恢复到下一次暂停
	
七、协程
	协程和线程的区别：
		○ 协程是异步的，线程是同步的
		○ 协程是非抢占式的，线程是抢占式的
		○ 线程是被动调度的，协程是主动调度的
		○ 协程可以暂停函数的执行，保留上一次调用时的状态，是增强型生成器
		○ 协程是用户级的任务调度，线程是内核级的任务调度
		○ 协程适用于IO密集型程序，不适用于CPU密集型程序的处理

	异步编程
		Python3.5 版本引入了await取代 yield from方式
		
			import asyncio
			# python3.5 增加async await
			async def py35_func():
			    await sth()
		注意：await 接受的对象必须是awaitable对象
		awaitable对象定义了__await__()方法
		
		awaitable对象有三类：
		1.协程 coroutine
		2.任务 task
		3.未来对象 future
		
		# 协程调用过程： 
		# 调用协程时，会被注册到ioloop，返回coroutine对象
		# 用ensure_future 封装为Future对象
		# 提交给ioloop
		

