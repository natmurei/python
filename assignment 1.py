Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[1,2,3,4,5,6,7,8,9]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x=[ :5]
SyntaxError: invalid syntax
>>> x.pop()
9
>>> x
[1, 2, 3, 4, 5, 6, 7, 8]
>>> x.append(10)
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 10]
>>> x.remove(5)
>>> x
[1, 2, 3, 4, 6, 7, 8, 10]
>>> x.count(8)
1
>>> x
[1, 2, 3, 4, 6, 7, 8, 10]
>>> x.extend([3])
>>> x
[1, 2, 3, 4, 6, 7, 8, 10, 3]
>>> x.reverse()
>>> x
[3, 10, 8, 7, 6, 4, 3, 2, 1]
>>> x.sort()
>>> x
[1, 2, 3, 3, 4, 6, 7, 8, 10]
>>> x.insert(5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x.insert(5)
TypeError: insert() takes exactly 2 arguments (1 given)
>>> x.insert(5,5.5)
>>> x
[1, 2, 3, 3, 4, 5.5, 6, 7, 8, 10]
>>> x.index(7)
7
>>> 
