学习笔记
面向对象编程：
	类两大成员：属性和方法
	Python2.2以前类叫经典类，类是单独的部分，基本数据类型是另外的部分，类实现功能很难统一；Python2.2以后类叫新式类，会继承Object类，和现有的基本数据类型同源
一、属性：
	类属性和对象属性
	类属性 字段在内存中只有一份，当有多个引用，节省了内存
	对象属性 在每个对象都保存一份，当数据在不同作用域下需要存储多份数据
	
	
	1.class Human(object):
	    # 静态字段
	    live = True
	    def __init__(self, name):
	        # 普通字段
	        self.name = name
	
	
	2.__dict__都可以取到作用域里面定义的所有属性
	
	3.注意！
		# 实例可以使用普通字段也可以使用静态字段
		#如果实例引用一个不存在的属性，python会自动创建这个属性
		man.name
		man.live = False
		#False
		man.live
		
		#woman也可以访问到新创建的属性，因为是Human的实例，所以访问到live=True
		woman.live
		
		# 类可以使用静态字段
		Human.live
	
	4.区分类是否为同一个对象
		type(a)
		id(a)
		a.__class__()
	
	5.查看类的属性：
		dir(Human) 列表的形式来查看属性
		Human.__dict__
		
		# 内置类型不能增加属性和方法
		setattr(list, 'newattr', 'value')
		
		当对一个实例的属性去修改的时候，不会影响其他实例
	
	5.三种不同下划线命名的属性：
		class Human2(object):
		    # 人为约定不可修改，常为内部属性，中间值属性，可见不修改
		    _age = 0
		    # 私有属性，防止人为修改或程序误修改，可以访问到但是不推荐访问
		    __fly = False
		    # 魔术方法，不会自动改名，跟随系统发生变化
		    # 如 __init__
		
		# 自动改名机制
		Human2.__dict__
		
		显示object类的所有子类
		print( ().__class__.__bases__[0].__subclasses__() )
		
		type(()) 是个元组
		().__class__.__bases__类的父类是object
		().__class__.__bases__[0]从tuple中把元素释放，object类

二、方法
分类：
	• 普通方法（实例方法）至少一个self参数，表示该方法的对象
	• classmethod类方法   至少一个cls参数，表示该方法的类
	• staticmethod静态方法     由类调用，无参数

后两种属于语法糖：原有语法基础上增加特殊功能 @classmethod


classmethod 相当于一个构造函数，类中只有一个构造函数__new__，所以产生classmethod

	实例和类都可以使用
	如果实例没有该属性就去找类的属性
	
	classmethod好处：p5_1classmethod.py
	1.在父类中定义classmethod，子类需要根据自己的变量名称发生变化，这里子类和父类id不同
	2函数需要调用类中的方法并返回，提前做预处理
	
staticmethod  没有参数self 和 cls，不能用到类和实例的属性
作用：某个功能频繁使用，如类型转换；增加某些特定的判断

两者区别：
staticmethod没有参数self 和 cls，不能用到类和实例的属性，主要用于额外处理的逻辑
classmethod主要作为构造函数

三、高级描述器
1.对实例获取属性：
	  __getattribute__()： 对所有属性的访问都会调用该方法
	  __getattr()：适用于未定义的属性
	
	如果这俩方法同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__
	注意：
	1.无论属性是否存在都会调用__getattribute__，损耗性能
	2.调用完__getattr__,利用hasattr判断属性能返回true，但是dict里依然没有属性，这两者不一致

2.属性描述符property   是一个类，
功能：1）把方法封装成属性
	  2）读写分离，分权限控制property
property类需要实现__get__、__set__、__delete__

# property本质并不是函数，而是特殊类（实现了数据描述符的类）
# 如果一个对象同时定义了__get__()和__set__()方法，则称为数据描述符，
# 如果仅定义了__get__()方法，则称为非数据描述符
# property的优点：
# 1 代码更简洁，可读性、可维护性更强。
# 2 更好的管理属性的访问。
# 3 控制属性访问权限，提高数据安全性。

四、面向对象编程
	继承，Python支持单继承，也支持多继承（missing解决）
	新式类，所有类都继承一个父类，Object类
	
	object和type的关系：
		○ object和type都属于type类，都由元类type创建
		○ object的父类为空，没有继承任何类
		○ type的父类是object类
	
类的继承
	• 单一继承
	• 多重继承
	• 菱形继承（钻石继承）：去父类找，父类没有就去父类的父类去找
	• 继承机制MRO
	• MRO的C3算法

	# 问题1 子类中没有定义的父类中的属性有没有被继承？没有被继承
	# 问题2 能否实现多重层级继承？能
	# 问题3 能否实现多个父类同时继承？能
	
	# 广度优先， 另外Python3 中不加(object)也是新式类，但是为了代码不会误运行在python2下产生意外结果，仍然建议增加
	#  查看继承顺序      Subclass.mro()
	
	多重继承的顺序问题：
		有向无环图：DAG，常被用于处理动态规划，寻求最短路径的场景

重载：python没有实现重载

五、solid设计原则与设计模式（22个）：
	解决编写项目时类如何进行拆分，方法如何拆分，哪些方法合并，哪些抽象，哪些用property
	
SOLID设计原则
	• 单一责任原则 The Single Responsibility Principle
	• 开放封闭原则 The Open Closed Principle     classmethod
	• 里氏替换原则 The Liskov Subsitituion Principle    基础功能放在父类，特殊功能放在子类
	• 依赖倒置原则 The Dependency Inversion Principle  高层不能依赖低层，利用抽象
	• 接口分离原则 The Interface Segregation Principle    如请求HTTP不需要考虑TCP
后两条与python有些相违背

单例模式：
	1.对象只存在一个实例
	2.__init__ 和 __new__ 区别：
		○ __new__在实例创建之前被调用，返回该实例对象，是静态方法
		○ __init__ 是实例对象创建完成后被调用，是实例方法
		○ __new__先被调用， __init__后被调用
		○ __new__的返回值（实例）将传递给__init__方法的第一个参数， __init__给这个实例设置相关参数
	3.创建方式：
		○ 装饰器方式，不考虑多线程
		○ __new__，引入多线程机制，如果单例用在多线程中，要加锁
		○ Import,最安全最保险
	
工厂模式：
	1.简单（静态）工厂模式: 根据创建的不同参数，创建不同的实例
		三种角色：
			工厂角色，产生实例，判断输入的参数
			抽象产品角色，创建所有对象的父类，父类来提供公共的接口，Human类
			具体产品角色，有不同的属性，Man和Woman类
		
	2.类工厂模式：动态的创建类
	
六、元类    （通常写框架时才写元类）
	• 元类是创建类的类，是类的模板
	• 控制如何创建类
	• 元类的实例为类，正如类的实例为对象
	• 创建元类的两种方法：type,class

# 元类要求,必须继承自type    
class DelValue(type):
    # 元类要求，必须实现new方法
    def __new__(cls,name,bases,attrs):
        attrs['pop_value'] = pop_value
        return type.__new__(cls,name,bases,attrs)
 
class DelDictValue(dict,metaclass=DelValue):
    # python2的用法，在python3不支持
    # __metaclass__ = DelValue
    pass

七、抽象基类 abstract base class ABC  用来确保派生类实现了基类中的特定方法
	好处：
		○ 避免继承错误，使类层次易于理解和维护
		○ 无法实例化基类
		○ 如果忘记在其中一个子类中实现接口方法，要尽早报错
		
	Mixin模式：在程序运行过程中，重新定义类的继承，即动态继承
		好处：
			○ 可以在不修改任何源代码的情况下，对已有类进行扩展
			○ 进行组件的划分






