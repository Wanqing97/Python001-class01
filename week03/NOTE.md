学习笔记
1.Twisted 多任务，异步框架
2.多进程：同步的系统
Os.fork()  研究底层原理
Multiprocessing.Process()
注意进程的父子关系

3.如果运行的方式是python XX.py，那么会从main方法开始执行
如果该文件被import，那么main方法不会被执行

4.锁保证资源的抢占问题

5.进程与线程的区别：
多进程十分消耗资源开销，所以用到线程

6.同步与异步：接受方看到的结果
阻塞与非阻塞：发起方看到的结果

7.为什么有多进程还要有多线程：
python多线程只能在一个CPU上去进程， 希望python在多个CPU进行所以使用多进程

8.并行和并发
并行：有两个CPU核心有两个队列

9.拿到GIL锁才可以使用CPU
I/O 读写操作，读写磁盘，读写数据包
线程遇到I/O操作会释放GIL锁，让其他线程抢夺资源

普通/多线程/多进程： 
多核/多进程最快，说明在同时间运行了多个任务。 
多线程的运行时间居然比什么都不做的程序还要慢一点，说明多线程还是有一定的短板的（GIL）。

多线程优势：适用于I/O密集型
