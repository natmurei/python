Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[0,1,2,3,4,5,6,7,8,9,]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y=[n*10 for n in x]
>>> y
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> for p in x
SyntaxError: invalid syntax
>>> for p in x:
	print(p*10)

	
0
10
20
30
40
50
60
70
80
90
>>> k=x[ :5]
>>> k
[0, 1, 2, 3, 4]
>>> v=x[4: ]
>>> v
[4, 5, 6, 7, 8, 9]
>>> v=x[5: ]
>>> v
[5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> n[[,2,3],[4,5,6],[7,8,9]]
SyntaxError: invalid syntax
>>> n[[1,2,3],[4,5,6],[7,8,9]]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    n[[1,2,3],[4,5,6],[7,8,9]]
NameError: name 'n' is not defined
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>> m={}
>>> for sublist in n:
	for x in sublist:
		m.append(x)

		
Traceback (most recent call last):
  File "<pyshell#29>", line 3, in <module>
    m.append(x)
AttributeError: 'dict' object has no attribute 'append'
>>> m=[]
>>> for sublist in n:
	for x in sublist:
		m.append(x)

		
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
