#append
x = ['shun','katu','hav']   #добавляет в конец списка элемент
x.append('tutak')
print(x)


#clear
x = ['shun','katu','hav']   #удаляет все элементы из списка
x.clear()
print(x)


#copy
x = ['shun','katu','hav']    # копия списка
y = x.copy()
y[-1] = 3                    # в копированном списке меняем элемент
print(x)
print(y)

#count
count= [1,2,5,8,5,5]          #возврошает сколко данного элемента есть в списке
print(count.count(5))

#extend
x = ['shun','katu','hav']        #добавkztn элементы списка в другой список
m = ['xoz','dzi']
x.extend(m)
print(x)

#index                             #возвращает индекс указанного элемента в списке
index= ['a','b','c']
print(index.index('b',0 , -1))     #list.index(element, start, end)

#insert
i= ['a','b','c']             #вставляет элемент в список по указанному индексу
i.insert(1,'z')
print(i)


#pop
print(index.pop(1))         #етод pop() в Python выводит последний элемент в списке, если не передан параметр.(1)
print(index)


#remove
list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']  #удаляет первый совпадающий элемент из списка.
list.remove('Mars')
print(list)


#reverse
list1 =[12, 'three', 7, 14, 1, 12, 'Mars']  #Перестраивает элементы списка в обратном порядке
list1.reverse()
print(list1)



#sort
a=[1,-45,3,2,100,-4]                 #сортирует элементы списка в порядке возрастания.
a.sort()
print(a)