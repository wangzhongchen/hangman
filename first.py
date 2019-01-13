"""
可以使用python处理文件，比如读取或者写文件数据。
"""

#写文件操作
"""
1.内置函数open打开文件。
文件路径，文件在计算机中所处的位置。

若文件路径中只有文件的名字，自动在程序所处的目录下查找文件。

r:只读,不存在，报错；
w：只写，文件存在，覆盖之；不存在，创建之；
w+：可读可写

import os
#os模块来构建文件路径，避免在不同os上出错
#print(os.path.join("Users","bob","1.txt"))#Users\bob\1.txt

#f = open("1.txt","r")#f：文件对象

#print(f.read())#FileNotFoundError: [Errno 2] No such file or directory: '1.txt'
#f.close()


with open("1.txt","w") as f:#自动关闭文件
    f.write("hello\n""world")

with open("1.txt","r") as f:
    print(f.read())
    #hello
    #world
    print(type(f.read()))#<class 'str'>包含文件所有行的可迭代对象

li = list()
with open("1.txt","r") as f:
    li.append(f.read())
    print(li)#['hello\
    #li.append(f.readline())
    #print(li)  # ['hello\n']
    

"""


#CSV文件
import csv
#csv文件，逗号分隔数据，常用在管理报表的程序中

with open("2.csv","w") as f:
    w = csv.writer(f,delimiter = ",")#返回一个csv对象
    w.writerow(["1","2","3"])#只创建一行数据，每个元素代表一个单元格
    w.writerow(["4","5","6"])

with open("2.csv","r") as f:
    r = csv.reader(f,delimiter = ",")#返回一个csv对象
    for row in r:
        #print(type(row))#<class 'list'>
        #print(row)#['4', '5', '6']
        print(",".join(row))
"""
1,2,3

4,5,6
"""


