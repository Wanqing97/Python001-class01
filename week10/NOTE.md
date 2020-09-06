学习笔记
做毕设过程中遇到的之前没遇到或之前没记录的问题：
1.
Q：ModuleNotFoundError: No module named 'MySQLdb'

A：pip3 install mysqlclient

2.Q： import mysql.connector
A： pip install mysql-connector

3.做情感分析重新创建一张新表sentiments写数据时
1）Q： 'charmap' codec can't encode characters in position 0-1: character maps to <undefined>
A： engine = create_engine(
        f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset="utf-8"',
        echo=False
    )

2）在此基础上又报了错
Q：Fisqlalchemy.exc.OperationalError: (MySQLdb._exceptions.OperationalError) (2019, 'Can\'t initialize character set "utf-8" (path: compiled_in)')
(Background on this error at: http://sqlalche.me/e/13/e3q8)
意识到自己的数据库字符集是utf8mb4依然报错不能初始化
把双引号去掉，最终版：
engine = create_engine(
        f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4',
        echo=False
    )
4.
Q： Django报错[WinError 123] 文件名、目录名或卷标语法不正确。: '<frozen importlib._bootstrap

A： 当你在项目文件中删除app对应的文件
却没有在项目url中删除之前配置的路径
也没有删除setting中配置的app




