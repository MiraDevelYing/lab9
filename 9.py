import numpy as np
import random
import timeit #імпортуємо модуль для підрахунку часу 
while True:
 vvod=input('Як вводити ? Якщо ранломно -1,якщо з клавіатури- будь яка клавіша')  #Вибираємо одне із значення для нашої змінної
 metod=input('Яким методом? бульбашковим -1,вібирка-2,вставками-будь яка клавіша')
 sortirovka=input('Как сортировать?Если по возрастанию-1,если по убыванию-любая копка')
 def bubl_up(s): #заводимо функції для бульбашкового метода,для сортиртування по збільшенню,де s-це кількість елементів(s-обов'язвокий елемент)
    global count #Заводимо 2 лічильника і робимо їх глобальними щоб їх можна було викликати в подальшій функціїї оцінки роботи
    global obmen
    count=0
    obmen=0
    for i in range(1,n): #Сам бульбашковий алгоритм
        for j in range(n-1,i-1,-1):
            count+=1
            if (A[j-1]>A[j]):
                obmen+=1
                A[j],A[j-1]=A[j-1],A[j]
    print(A)
 def bubl_down(s):#заводимо функцію для бульбашкового метода,для сортування по зменшеннню
    global count
    global obmen
    count=0
    obmen=0
    for i in range(1,n):
        for j in range(n-1,i-1,-1):
            count+=1
            if (A[j-1]<A[j]):
                obmen+=1
                A[j],A[j-1]=A[j-1],A[j]
    print(A)
 def select_up(s):#заводимо функцію для алгоритма сортування метода вибору,для сортування по зібльшенню 
    global count_se
    global obmen_se
    count_se=0
    obmen_se=0
    for i in range(n-1):#cам алгоритм вибору
        min=i
        for j in range(i+1,n):
            count_se+=1
            if A[j]<A[min]:
                obmen_se+=1
                min=j
        A[i],A[min]=A[min],A[i]
    print(A)
 def select_down(s):#заводимо функцію для алгоритма сортування метода вибору,для сортування по зменшенню
    global count_se
    global obmen_se
    count_se=0
    obmen_se=0
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            count_se+=1
            if A[j]>A[min]:
                obmen_se+=1
                min=j
        A[i],A[min]=A[min],A[i]
    print(A)
 def insertion_up(s):#заводимо функцію для алгоритма сортування метода вставки,для сортування по збільшенню
    global count_ins
    global obmen_ins
    count_ins=0
    obmen_ins=0
    for i in range(1,n):# сам алгоритм вставки
        j=i-1
        key=A[i]
        while j>=0 and A[j]>key:
            count_ins+=2
            obmen_ins+=1
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    print(A)
 def insertion_down(s):#заводимо функцію для алгоритма сортування метода вставки,для сортування по зменшенню
    global count_ins
    global obmen_ins
    count_ins=0
    obmen_ins=0
    for i in range(1,n):
        j=i-1
        key=A[i]
        while j>=0 and A[j]<key:
            count_ins+=2
            obmen_ins+=1
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    print(A)
        
 if vvod=='1': 
  x=int(input('Введіть кількість цифр'))
  A=np.zeros(x,dtype=int) #Заводимо масив,і заповняємо його рандомними значеннями
  for i in range(x):
   A[i]=random.randint(0,100000)
  print(A)
  n=len(A)
  s=x
 else:#якщо значення vvod !=1,то ми заповняємо наш масив сами,до 30 значень
   x=int(input('Введіть кількість цифр'))
   while x>30:
      x=int(input('Введіть кількість цифр  до 30'))
   A=np.zeros(x,dtype=int)
   for i in range(x):
    A[i]=int(input('Введіть число '))
   print(A)
   n=len(A)
   s=x
 def xarakteristika_bubl(countner): #Заводимо функцїї для оцінки роботи для кожного з методів
    print('Кількість порівнювань бульбашкового метода',countner)
    print('Кількість обмінів бульбашкового метода',obmen)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)#Присвоюємо t,значення часу за який працював кожний алгоритм 
    print('Программа виконується',t)
 def xarakteristika_select(countner):
    print('Кількість порівнювань метода вибору',countner)
    print('Кількість обмінів метода вибору',obmen_se)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Программа виконується',t)
 def xarakteristika_ins(countner):
    print('Кількфсть порівнювань метода вставками',countner)
    print('Кількість обмінів метода вставками',obmen_ins)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Программа виконується',t)
 if metod=='1': #В залежності від вибраних значень виводимо наші функціїї 
  if sortirovka=='1':
    bubl_up(s)
    xarakteristika_bubl(countner=count)#counter являється поіменованим параметром функції
  else:
    bubl_down(s)
    xarakteristika_bubl(countner=count)
 elif metod=='2':
     if sortirovka=='1':
         select_up(s)
         xarakteristika_select(countner=count_se)
     else:
         select_down(s)
         xarakteristika_select(countner=count_se)
 else:
    if sortirovka=='1':
        insertion_up(s)
        xarakteristika_ins(countner=count_ins)
    else:
        insertion_down(s)
        xarakteristika_ins(countner=count_ins)
 result = input('Бажаєте продовжити? Якщо да - 1, Если ні - інше: ') #зациклюємо нашу программу
 if result == '1':
   continue
 else:
   break
