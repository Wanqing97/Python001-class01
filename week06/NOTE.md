学习笔记
一、Django特点：
1.采用MTV框架（与MVC区别：MVC设计模式，指导思想，没办法直接用）
	MTV框架，模型，模板，视图
	流程：1）浏览器输入网址和服务器请求，2）服务器转给view视图接受请求，3）然后调用models模型调用数据，4）调用templates模板进行展示，5）再和models的数据相结合给浏览器端返回响应。
2.强调快速开发和 代码复用（DRY原则，Do Not repeat yourself，Django提供很多组件来解决代码复用问题）
3.组件丰富：
	ORM对象关系映射，类和对象的方式替代sql处理数据的方式
	URL支持正则表达式
	admin管理系统
	模板可继承
	内置用户认证，提供用户认证和权限功能
	内置表单模型、Cache缓存系统、国际化系统等
	
二、参考https://www.cnblogs.com/datascientist/p/3550174.html
安装：（注意版本问题，最新3.0还不稳定，建议2.2）
	pip3 install Django==2.2.13 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

查看django版本：
	python -m django --version

启动：
	必须把MTV模型写好，并且一直是web服务器的形式，不是响应一次就结束
	1.创建Django项目 
		django-admin.py startproject MyDjango
		⽬录结构如下： 
			MyDjango/manage.py 命令⾏⼯具  整个项目管理
			MyDjango/MyDjango 
			MyDjango/MyDjango/__init__.py 
			MyDjango/MyDjango/settings.py        项⽬的配置⽂件 
			MyDjango/MyDjango/urls.py 
			MyDjango/MyDjango/wsgi.py
		
	2.创建应用程序   利用manage.py
		cd MyDjango
		
		python manage.py help 查看具体功能
		
		python manage.py startapp index 会创建index文件夹
			index/migrations 数据库迁移文件夹 
			index/models.py  模型 
			index/apps.py 当前app配置文件
			index/admin.py 管理后台 
			index/tests.py 自动化测试 
			index/views.py 视图
	3.真正启动
		python manage.py runserver
		…
		Django version 2.2.13, using settings 'MyDjango.settings'
		Starting development server at http://127.0.0.1:8000/
		Quit the server with CTRL-BREAK.
		
		实际工作中可以更改端口号 python manage.py  runserver 0.0.0.0:80   其他人可以访问
		
		Ctrl + c 结束Django开发环境
		
三、Django如何使用
配置文件：
	• 项目路径 • 密钥 • 域名访问权限 • App 列表 • 静态资源，包括CSS、JavaScript 图片等 • 模板文件 • 数据库配置 • 缓存 • 中间件
	
Settings.py
	没有导入过多的模块方便Django做迁移
	项目路径：Import os     os可以通过 dirname读取路径  os.path.dirname()
	密钥：用于生产环境部署，防止被别人入侵
	调试模式： DEBUG = True，打印大量调试日志，仅用于开发
		注意！单独运行的Django没法用于生产模式，仅支持单用户访问，如果有阻塞性操作，第二个用户会被阻塞。如果想用于生产模式加WSGI
	Installed_apps：默认支持哪些程序，不要随意更改顺序
	中间件：request和response对象之间的钩子hook，也有顺序问题
	模板：可以用外部的模板引擎，模板路径常常在index目录里配置
	数据库配置：默认sqlite数据库
	以上必须修改两部分：apps和数据库

四、URL调度器 URLConf
Django如何处理一个请求：
	1.如果传入HTTPRequest对象拥有urlconf属性（通过中间件设置），它的值会被ROOT_URLCONF 代替。（去urls.py文件里找）
	2.Django加载URLConf模块并寻找可用的urlpatterns，Django依次匹配每个URL模式，在与请求的URL匹配的第一个模式停下来。
	3.一旦有URL匹配成功，Django导入并调用相关的视图，视图会获得参数：HTTPRequest实例和位置参数
	4.如果没匹配，调用适当错误处理视图
代码流程：
	1.增加项目 urls.py （.表示同级路径）------>2.views.py  返回HTTPResponse
	内部具体流程：
	Manage.py------------------------------------------------------------------------------------>settings.py找ROOT_URLCONF='MyDjango.urls'------------------------>MyDjango文件夹里的urls.py找到path('',include('index.urls'))，这里index配置在apps里--------------------------->index文件夹里的urls.py找到
	path('',views.index) ----------------->views.py

五、模块和包
模块  .py结尾的python文件
	def func1():
	    print('import func1')
	
	if __name__ == '__main__':
	    func1()
	
包 存放多个模块的目录
__init__.py 优先运行

导入包：
Import Package  （不写默认从python的安装目录 site-packages引入）C:\Users\wwqqw\AppData\Local\Programs\Python\Python37\Lib\site-packages
From Package import Module as M
	从当前目录引入   from . Import Module1
	从当前目录的包引入 from .Pkg2 import M2

六、Django连接数据库遇到的问题：

1.# 报错问题
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?
解决方法：__init__下设置：
		import pymysql
		pymysql.install_as_MySQLdb()

2.# 报错位置
File "G:\python\lib\site-packages\django\db\backends\mysql\base.py", line 36, in <module>
# 报错问题
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3
解决方法：点击报错位置找到这两行 注释掉
1）	version = Database.version_info
2）	# if version < (1, 3, 13):
3）	#    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

3.# 报错问题
 raise IOError("No translation files found for default language %s." % settings.LANGUAGE_CODE)
OSError: No translation files found for default language utf-8.
解决方法：Settings.py LANGUAGE_CODE = 'en-us'

4.# 报错问题
django.db.utils.OperationalError:(2003, "Can't connect to MySQL server on '127.0.0.1'
解决方法：
Settings.py 端口号8000改成3306，'PORT': '3306'

5.# 报错问题
File "C:\Users\wwqqw\AppData\Local\Programs\Python\Python37\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query
    query = query.decode(errors='replace')
AttributeError: 'str' object has no attribute 'decode'
解决办法：
query = query.encode('utf-8').decode(errors='replace')
中间加上.encode('utf-8')即可。
问题原因：
python3里面，字符串要先encode手动指定其为某一编码的字节码之后，才能decode解码。


七、URL支持变量：可以限制url的类型，长度，自定义过滤器（正则等）
1.变量类型包括：str,int, slug备注, uuid唯一的id, path
	path('<int:year>', views.year), 
2.from django.urls import path, re_path
3.支持正则表达式 
	re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
4.**kwargs关键字参数，用于接收多个参数
5.register_converter自定义过滤器
	一个类必须含三部分：
	    1.regex = '[0-9]+'
	    2.def to_python(self, value):
	    3.def to_url(self, value):
注意要匹配的内容不能重复，从上到下运行，如果上面匹配过，后面不会再执行

八、view视图：关注处理完成后，如何返回
1.正常返回指定错误码用HTTPResponse
2.快捷函数：
	render() 是把返回的html内容写入到专门的文件中，这个文件还支持导入变量
		默认去templates文件夹找html，手动创建
	Redirect() HTTPResponseRedirect ，重新解析url
	Get_object_or_404() 从模型取数据，数据不存在返回404。将view视图和模型做了绑定

九、ORM创建表 和 API
python manage.py makemigrations    生成中间脚本应用到数据库
python manage.py migrate   
这样就能通过model来自动映射生成数据库，里面的一个类就是一张数据表（ORM）
自动生成的表命名规则：app名称小写_model类名小写 appname_modelname

找不到mysql配置文件：
解决方法：export PATRH$PATH:/usr/local/mysql/bin

增删改查用api
Manage.py启动shell
python manage.py shell

详细语句见ORM_API.txt

十、模板开发
通过if可以动态的改变模板的展示

十一、MTV流程：
http://127.0.0.1:8000/books
manage.py 接收到请求
项目下的urls.py
index下的urls.py
index下的views.py找到books()       获取所有本地变量函数locals()，传到模板
						     index下的models.py找到Name类

十二、models配置
正向过程：原生项目通过ORM方式创建数据，
反向过程：数据采集等工作，反向从MySQL表创建回Django的model
python manage.py inspectdb > models.py
此文件注意两点：
	1.会自动生成Meta元类，不属于任何一个字段的数据
		managed = False 表示不能通过ORM转化表了,不能创建等等，防止数据冲突
	2.配置好MySQL连接

十三、sql文件导入到mysql中
 source G:/git_code/pythontrain/t1.sql

使用filter函数必须要把从mysql查到的数据放入 queryset

if __name__ == '__main__':
    main()
python manage.py    运行main函数，做为模块
import manage.py    不会运行main函数

python manage.py runserver 8080
1.解析runserver 8080等参数
2.加载runserver的文件
3.检查app，ip端口有没有被占用，ORM设置
4.实例化WSGIserver
5.动态创建一些类，为了接收请求

遇到的坑：
1.往mysql导入t1.sql时，没注意到t1.sql文件里创建了新的数据库db1,代码与mysql里表实际存在的库不一致导致执行django时报表不存在
2.ORM 创建表
python manage.py makemigrations
python manage.py makemigrations Douban （app_name）
端口号不一致
3.ORM没有自动创建表：提示No migrations to apply.
解决方法：
找到django_migrations表，删除该app名字的所有行。
重新执行makemigrations 和 migrate
4.FieldError at /douban/search
Cannot resolve keyword 'title' into field.
解决方法：如果想过滤字符串，filter的参数：字段名__icontains
MovieInfo.objects.filter(comment__icontains=s)

