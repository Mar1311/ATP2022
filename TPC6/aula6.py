import csv
from turtle import color
import matplotlib.pyplot as plt


def ordem(tuplo):
    return tuplo[0]


def lerobras():
    file = open("obras.csv", encoding="UTF8") 
    file.readline()
    csv_file = csv.reader(file, delimiter=";")
    lst0 = []
    for line in csv_file:
        lst0.append(tuple(line))
    return lst0

def count():
    lst = list(lerobras())
    return len(lst)

def imp(obras):
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
    for nome, des, ano,_, comp, *_ in obras:
        print(f"| {nome[:20]:20} | {des[:25]:10} | {ano:8} | {comp[:15]:15} |")

def ordemt(tuplos):
    return tuplos[0]
def ordenaralfa(obras):
    lst = []
    for nome,_, ano, *_ in obras:
        lst.append((nome, ano))
    lst.sort(key=ordemt)
    return lst

def ordem(tup):
    return tup[1]
def ordenarc(obra):
    lst1 = []
    for nome,_, ano, *_ in obra:
        lst1.append((nome, ano))
    lst1.sort(key=ordem)
    return lst1

def distPeriodo(obras):
    dici = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else:
            dici[periodo] = 1
    return dici  

def distAno(obras):
    dic = {}
    for _, _, ano, *_ in obras:
        if ano in dic.keys():
            dic[ano] = dic[ano] + 1
        else:
            dic[ano] = 1
    return dic

def distituloAno(obras):
    dici = {}
    for nome, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)
        else:
            dici[ano] = [nome]
    return dici

def disObrasComp(obras):
    dici = {}
    for nome, _, _, _, comp, *_ in obras:
        if comp in dici.keys():
            dici[comp].append(nome)
        else:
            dici[comp] = [nome]
    return dici

def compos(obras):
    dicion = {}
    for _,_,_,_,comp,*_ in obras:
        if comp in dicion.keys():
            dicion[comp] += 1
        else:
            dicion[comp] = 1
    return dicion


#distr periodo, ano e compositor

def distribuicaoP(obras): 
    plt.figure(figsize=(28,12))
    plt.bar(obras.keys(), obras.values(), color="purple")
    plt.xticks([x for x in range(0, len(obras.keys()))], obras.keys(), rotation= "vertical")
    plt.show()

def listaObrasComp(obras):
    newdict = zip(obras.keys(), obras.values())
    newlist = list(newdict)
    return newlist
