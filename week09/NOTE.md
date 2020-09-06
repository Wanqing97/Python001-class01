学习笔记
Django进阶
一、Django源码分析
1.URLconf
	A.偏函数：降低函数调用的难度。可以固定不必要的参数，只传需要的参数
		阅读源码的方法：
		1）典型写法：
		urlpatterns = [
		    path('', views.index),
		  re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
		]
		从源码层面对比path()与re_path()的区别
	
		2）#site-packages/django/urls/conf.py
		path = partial(_path, Pattern=RoutePattern)
		re_path = partial(_path, Pattern=RegexPattern)
		
		#官方文档 https://docs.python.org/zh-cn/3.7/library/functools.html
		3）
		# def partial(func, *args, **keywords):
		#     def newfunc(*fargs, **fkeywords):
		#         newkeywords = keywords.copy()
		#         newkeywords.update(fkeywords)
		#         return func(*args, *fargs, **newkeywords)
		#     newfunc.func = func
		#     newfunc.args = args
		#     newfunc.keywords = keywords
		#     return newfunc
		
		4）partial函数的实现
			§ 闭包（装饰器）
			§ 怎么实现参数处理的
			§ 除了实现功能，还考虑了哪些额外的功能
		5）
		# 官方文档demo
		# from functools import partial
		# basetwo = partial(int, base=2)
		# basetwo.__doc__ = 'Convert base 2 string to an int.'
		# basetwo('10010')
		# 18
		
		6）
		# 要注意：
		# 1.partial 第一个参数必须是可调用对象
		# 2.参数传递顺序是从左到右，但不能超过原函数参数个数
		# 3.关键字参数会覆盖partial中定义好的参数


	B.include:   可以把子项目中类型做一个拆分。
	#site-packages/django/urls/conf.py （此文件有path(), _path(), include()）
	def include(arg, namespace=None):
	    app_name = None
		#如果是元组类型进行拆分（'douban.index', 'douban'）
	    if isinstance(arg, tuple):
	        pass    
		#如果是字符串类型，获得两个新的属性并返回urlconf_module对象本身
	        if isinstance(urlconf_module, str):
	        urlconf_module = import_module(urlconf_module)
		patterns = getattr(urlconf_module, 'urlpatterns', urlconf_module)
	         app_name = getattr(urlconf_module, 'app_name', app_name)
	    if namespace and not app_name:
	        raise ImproperlyConfigured(
	            'Specifying a namespace in include() without providing an app_name '
	            'is not supported. Set the app_name attribute in the included '
	            'module, or pass a 2-tuple containing the list of patterns and '
	            'app_name instead.',
	        )
	    if isinstance(patterns, (list, tuple)):
	        pass
	    return (urlconf_module, app_name, namespace)
	
	C.import_module()
	D._path()

2.View视图
	A. 请求过程：(HttpRequest)
	Render 把HttpResponse又一次封装
	site-packages/django/http/request.py        Class QueryDict(MultiValueDict)
	site-packages/django/utils/datastructures.py        Class MultiValueDict（dict）
	
	url里传参，可使用QueryDict() 组成特殊的字典，key相同，传入的值不同
	QueryDict 引用父类 MultiValueDict，这其中的魔术方法有：__init__, __repr__, __getitem__, __setitem__
	B. 响应过程（HttpResponse）
	常用的属性和方法可以抽象成HttpResponse子类进行返回，如JsonResponse，HttpResponseNotFound，需要仔细查看文档
	C. 请求响应完整流程：
	四种类型代码：django自己实现的代码，程序员自己实现的功能，各种中间件，外部工具（浏览器，数据库）
	D. 
	字母表示扩展
	中间件不只是urls.py,views.py,models.py,template， 做全局处理


	Django框架和其他框架的区别：
		Django当产生一个新的请求时候，都带着HttpRequest这个类的对应的实例对象request，方便对每一次请求做判断，让整个请求过程非常的完备
		
3.Model模型的自增主键创建
	A. 为什么自定义的model要继承models.Model?
		○ 不需要显式定义主键
		○ 自动拥有查询管理器对象
		○ 可以使用ORM API对数据库、表实现CRUD

	# 作品名称和作者(主演)
	class Name(models.Model):
	    # id 自动创建
	    name = models.CharField(max_length=50)
	    author = models.CharField(max_length=50)
	    stars = models.CharField(max_length=5)
	
	id相关信息在ModelBase元类中  #site-packages\django\db\models\base.py
	 ModelBase类中的方法：
		○ __new__()创建新类
		○ add_to_class() 添加属性
		○ _prepare()

	objects类    #site-packages\django\db\models\options.py
		
	B. 查询管理器 Objects
	如何让查询管理器的名称不叫objects？
		from django.db.models import Manager
		class NewManger(Manager):
		    pass
		class T1(models.Model):
		    object = NewManger()
	
	如何利用Manager(objects)实现对Model的CRUD？
	为什么查询管理器返回QuerySet对象？
	
	Manager继承自BaseManagerFromQuerySet类，拥有QuerySet的大部分方法，get、create、filter等方法都来自QuerySet
	#site-packages\django\db\models\manager.py
	
4.template模板的加载文件
	A. 模板引擎怎么通过render()加载HTML文件？
	def books_short(request):
	    return render(request, 'result.html', locals())
	
	render()   #site-packages\django\shortcuts.py 
	def render(request, template_name, context=None, content_type=None, status=None, using=None):
	    """
	    Return a HttpResponse whose content is filled with the result of calling
	    django.template.loader.render_to_string() with the passed arguments.
	    """
	    content = loader.render_to_string(template_name, context, request, using=using)
	    return HttpResponse(content, content_type, status)
	
	render_to_string()     #site-packages\django\template\loader.py
	get_template()
	_engine_list()获取引擎 （默认引擎定义在settings.py的backend里）
	class EngineHandler:
	    @cached_property
	    def templates(self):
	        if self._templates is None:
	            self._templates = settings.TEMPLATES
	        # templates是有序字典
	        templates = OrderedDict()
	        backend_names = []
	        #遍历模板后端配置
	        for tpl in self._templates:
	            try:
	                # This will raise an exception if 'BACKEND' doesn't exist or
	                # isn't a string containing at least one dot.
	                default_name = tpl['BACKEND'].rsplit('.', 2)[-2]
	            except Exception:
	                invalid_backend = tpl.get('BACKEND', '<not defined>')
	                raise ImproperlyConfigured(
	                    "Invalid BACKEND for a template engine: {}. Check "
	                    "your TEMPLATES setting.".format(invalid_backend))
	            tpl = {
	                'NAME': default_name,
	                'DIRS': [],
	                'APP_DIRS': False,
	                'OPTIONS': {},
	                **tpl,
	            }
	            templates[tpl['NAME']] = tpl
	            backend_names.append(tpl['NAME'])
	            return templates
	B. 模板引擎怎样对模板进行渲染？
	 #site-packages\django\template\loader.py
	def get_template(template_name, using=None):
	    …
		# engine定义在初始化函数中，是Engine类的实例
	     # Engine类在site-packages\django\template\engine.py
		return engine.get_template(template_name)
	
	 #site-packages\django\template\engine.py
	class Engine:
	def get_template(self, template_name):
	        """
	        Return a compiled Template object for the given template name,
	        handling template inheritance recursively.
	        """
	        template, origin = self.find_template(template_name)
	        if not hasattr(template, 'render'):
	            # template needs to be compiled
	            template = Template(template, origin, template_name, engine=self)
	        return template
	def find_template(self, name, dirs=None, skip=None):
	        tried = []
	        for loader in self.template_loaders:
	            try:
	                # 通过get_template()获得template对象
	                template = loader.get_template(name, skip=skip)
	                return template, template.origin
	            except TemplateDoesNotExist as e:
	                tried.extend(e.tried)
	        raise TemplateDoesNotExist(name, tried=tried)
	
	#site-packages\django\template\backends\base.py
	class BaseEngine:
	 @cached_property
	    def template_dirs(self):
	        """
	        Return a list of directories to search for templates.
	        """
	        # Immutable return value because it's cached and shared by callers.
	        template_dirs = tuple(self.dirs)
	        if self.app_dirs:
	            template_dirs += get_app_template_dirs(self.app_dirname)
	        return template_dirs
	#site-packages\django\template\utils.py
	@functools.lru_cache()
	def get_app_template_dirs(dirname):
	    """
	    Return an iterable of paths of directories to load app templates from.
	    dirname is the name of the subdirectory containing templates inside
	    installed applications.
	    """
	    template_dirs = [
	        str(Path(app_config.path) / dirname)
	        for app_config in apps.get_app_configs()
	        if app_config.path and (Path(app_config.path) / dirname).is_dir()
	    ]
	    # Immutable return value because it will be cached and shared by callers.
	    return tuple(template_dirs)
	
	
	
	#site-packages\django\template\backends\django.py       
	class Templates:
		Return self.template.render(context)
		
	#调用了site-packages\django\template\backends\base.py  
	class Template：
	# source存储的是模板文件中的内容
	        self.source = str(template_string)  # May be lazy.
	        self.nodelist = self.compile_nodelist()
	
	如果是Node类型，则会调用render_annotated方法获取渲染结果，否则直接将元素本身作为结果，继续跟踪bit=node.render_annotated(context)
	#Node类的两个子类
	1)class TextNode(Node):
	    def render(self.context):
	        #返回对象（字符串）本身
	        return self.s
	
	2)class VariableNode(Node):
	    def render(self.context):
	        try:
	        #使用resolve()解析后返回
	            output = self.filter_expression.resolve(context)
	
	定义四种token类型：
	1）变量类型，开头为{{
	2）块类型，开头为{%
	3）注释类型，开头为{#
	4）文本类型，字符串字面值
		
	#site-packages\django\template\backends\base.py 
	class Lexer:

二、表单
1.#form.py
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)


2.python manage.py migrate 
这句命令会把admin需要的表同步到数据库中
INSTALLED_APPS = [
    ####  内置的后台管理系统
    'django.contrib.admin',
]

3.csrf防护
加token信息
如果用ajax也要记得参数加上token

三、用户管理验证
python manage.py shell
导入验证模块
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('jerry','jerry@jerry.com','jerrypassword')
>>> user
<User: jerry>
>>> user.save()

Settings.py
MIDDLEWARE = [
    'django.contrib.auth.middleware.AuthenticationMiddleware', #验证的中间件
]
运行此中间件，会写入数据库

>>> from django.contrib.auth import authenticate
>>> authenticate(username='jerry',password='jerrypassword')
<User: jerry>    有值说明用户名密码匹配
>>> authenticate(username='jerry',password='jerrypassword123')

四、信号
两个线程互相进行通知
	• 发生事件，通知应用程序
	• 支持若干信号发送者通知一组接收者
	• 解耦

内建新号有哪些？
https://docs.djangoproject.com/zh-hans/3.0/ref/signals

五、中间件（可以做很多请求中拦截的事情，偏底层功能）
	• 全局改变输入或输出
	• 轻量级的、低级的“插件”系统
	• 对请求、响应处理的钩子框架

	顺序：
	中间件请求
	中间件视图
	中间件响应
	
六、生产环境部署
HttpRequest     WSGIHandler       遵循WSGI协议
Apache转换器
Nginx + Django， 效率还是不够高
Tornado + Django
更高性能且配置更简单的装置：gunicorn

#安装gunicorn
pip install gunicorn

#在项目目录执行
gunicorn MyDjango.wsgi

报错：
G:\Python_code\Week009\MyDjango>gunicorn MyDjango.wsgi
Traceback (most recent call last):
  File "c:\users\wwqqw\appdata\local\programs\python\python37\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\users\wwqqw\appdata\local\programs\python\python37\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Users\wwqqw\AppData\Local\Programs\Python\Python37\Scripts\gunicorn.exe\__main__.py", line 4, in <module>
  File "c:\users\wwqqw\appdata\local\programs\python\python37\lib\site-packages\gunicorn\app\wsgiapp.py", line 9, in <module>
    from gunicorn.app.base import Application
  File "c:\users\wwqqw\appdata\local\programs\python\python37\lib\site-packages\gunicorn\app\base.py", line 11, in <module>
    from gunicorn import util
  File "c:\users\wwqqw\appdata\local\programs\python\python37\lib\site-packages\gunicorn\util.py", line 9, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'

Gunicorn --help
三个设置项：
-b 指定绑定的IP和对应的端口  默认127.0.0.1 8000
-w 默认一个进程（一个worker）
--access-logformat 日志的格式

七、项目中遇到的问题：
1.migration出错
	G:\Python_code\Week009\myWeb>python manage.py makemigrations UserAuth
	No changes detected in app 'UserAuth'

解决方法：
G:\Python_code\Week009\myWeb>python manage.py makemigrations --empty UserAuth
Migrations for 'UserAuth':
  UserAuth\migrations\0001_initial.py
该行命令目的是生成一个空的initial.py
再重新执行一遍migration和migrate命令

来自 <https://blog.csdn.net/chichu261/article/details/82868597> 



