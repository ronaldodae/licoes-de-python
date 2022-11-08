Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: C:/Users/ronal/Desktop/pasta do python/licao 2.py ==========
1
2
3
6
40
lista2.append(2)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    lista2.append(2)
AttributeError: 'int' object has no attribute 'append'
lista2=(1, 9, 3, 4, 2, 7, 6)
print(lista)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(lista)
NameError: name 'lista' is not defined. Did you mean: 'lista2'?
print(lista2)
(1, 9, 3, 4, 2, 7, 6)
>>> lista2.sort()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    lista2.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> lista2.count(1)
1
>>> lista2.reverse()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    lista2.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> lista2._reverse()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    lista2._reverse()
AttributeError: 'tuple' object has no attribute '_reverse'
