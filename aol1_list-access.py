# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:19:57 2023

@author: t-jan
"""
import random
import matplotlib.pyplot as plt

a = 100
koszt=0
Lista=[]
counters=[]

def move_to_front(lista,x):
    lista.insert(0, lista.pop(lista.index(x)))
    return lista

def transpose(lista,x):
    if lista.index(x)==0: return lista
    lista.insert(x-1, lista.pop(lista.index(x)))
    return lista

def access(x, lista, organizacja):
    if organizacja=='mtf':
        for i in range(0,len(lista)):
            if lista[i]==x:
                move_to_front(lista,x)
                return i+1
        lista.append(x)
        move_to_front(lista,x)
        return len(lista)-1
    elif organizacja=='t':
        for i in range(0,len(lista)):
            if lista[i]==x:
                transpose(lista,x)
                return i+1
        lista.append(x)
        transpose(lista,x)
        return len(lista)-1
    elif organizacja=='brak':
        for i in range(0,len(lista)):
            if lista[i]==x:
                return i+1
        lista.append(x)
        return len(lista)-1
    elif organizacja=='count':
        for i in range(0,len(lista)):
            if lista[i]==x:
                counters[i]+=1
                if i!=0:
                    for j in range(i,0,-1):
                        if counters[j-1]<counters[j]:
                            lista[j],lista[j-1] = lista[j-1],lista[j]
                            counters[j],counters[j-1] = counters[j-1],counters[j]
                return i+1
        lista.append(x)
        counters.append(1)
        return len(lista)-1
    else: return 'nieznana samoorganizacja'

def random_number(rozklad): # <1,100>
    prawdopodobienstwa=[]
    przedzialy=[]
    if rozklad=='jednostajny' or rozklad=='j':
        for i in range(0,100):
            prawdopodobienstwa.append(1/100)
    elif rozklad=='harmoniczny' or rozklad=='h':
        for i in range(1,101):
            prawdopodobienstwa.append(1/(i*5.1873775176396202608051))
    elif rozklad=='dwuharmoniczny' or rozklad=='d' or rozklad=='dh':
        for i in range(1,101):
            prawdopodobienstwa.append(1/(i**2*1.63498390018489286507716949818))
    elif rozklad=='geometryczny' or rozklad=='g':
        for i in range(1,100):
            prawdopodobienstwa.append(1/2**i)
        prawdopodobienstwa.append(1/2**99)
    else: return 'nieznany rozklad'
    przedzialy.append(0)
    przedzialy.append(prawdopodobienstwa[0])
    for i in range(2,len(prawdopodobienstwa)+1):
        przedzialy.append(przedzialy[i-1]+prawdopodobienstwa[i-1])
    przedzialy.append(1)
    X=random.random()
    for i in range(0,len(przedzialy)):
        if X>=przedzialy[i] and X<przedzialy[i+1]:
            return i+1

n=[100, 500, 1000, 5000, 10000, 50000, 100000]
koszt=[]
rozklad='j'
for i in range(0,len(n)):
    koszt.append(0)
c=0
for x in n:
    for op in range(0,x):
        liczba=random_number(rozklad)
        koszt[c]+=access(liczba, Lista, 'brak')
    c+=1
for p in range(0,len(n)):
    if p==0:
        plt.scatter(n[p],koszt[p],color='b',label='brak samoorganizacji')
    else:
        plt.scatter(n[p],koszt[p],color='b')
c=0
koszt=[]
for i in range(0,len(n)):
    koszt.append(0)
Lista=[]
for x in n:
    for op in range(0,x):
        liczba=random_number(rozklad)
        koszt[c]+=access(liczba, Lista, 'mtf')
    c+=1
for p in range(0,len(n)):
    if p==0:
        plt.scatter(n[p],koszt[p],color='crimson',label='move-to-front')
    else:
        plt.scatter(n[p],koszt[p],color='crimson')
c=0
koszt=[]
for i in range(0,len(n)):
    koszt.append(0)
Lista=[]
for x in n:
    for op in range(0,x):
        liczba=random_number(rozklad)
        koszt[c]+=access(liczba, Lista, 't')
    c+=1
for p in range(0,len(n)):
    if p==0:
        plt.scatter(n[p],koszt[p],color='yellow',label='transpose')
    else:
        plt.scatter(n[p],koszt[p],color='yellow')
c=0
koszt=[]
for i in range(0,len(n)):
    koszt.append(0)
Lista=[]
for x in n:
    for op in range(0,x):
        liczba=random_number(rozklad)
        koszt[c]+=access(liczba, Lista, 'count')
    c+=1
for p in range(0,len(n)):
    if p==0:
        plt.scatter(n[p],koszt[p],color='limegreen',label='count')
    else:
        plt.scatter(n[p],koszt[p],color='limegreen')

plt.xlabel('n')
plt.ylabel('koszt n operacji')
plt.legend()
if rozklad=='j':
    plt.title('Rozkład jednostajny')
elif rozklad=='h':
    plt.title('Rozkład harmoniczny')
elif rozklad=='d':
    plt.title('Rozkład dwuharmoniczny')
elif rozklad=='g':
    plt.title('Rozkład geometryczny')
plt.show()
