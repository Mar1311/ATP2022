import csv
import matplotlib.pyplot as plt

def ler():
    file = open("alunos.csv", encoding="utf8")
    file.readline()
    csv_file = csv.reader(file, delimiter=",")
    lst0 = []
    for line in csv_file:
        lst0.append(tuple(line))
    return lst0

def countalunos():
    lst = list(ler())
    return len(lst)

#alunos por curso:
def alcurso(alunos):
    dic = {}
    for _,_,curso, *_ in alunos:
        if curso in dic.keys():
            dic[curso] += 1
        else:
            dic[curso] = 1
    return dic

#média de cada aluno  [(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4)]
def media(alunos):
    lst1 = []
    for _, nome, _, t,p,c,v, *_ in alunos:
        media = (int(t)+int(p)+int(c)+int(v))/4
        lst1.append((nome, media))
    dici = dict(lst1)
    return dici

def distribuicaoP(alunos, titulo, abcissa, ordenada): 
    plt.figure()
    plt.bar(alunos.keys(), alunos.values(), color="yellow")
    plt.xticks([x for x in range(0, len(alunos.keys()))], alunos.keys(), rotation= "vertical")
    plt.ylabel(ordenada, rotation= 'vertical')
    plt.xlabel(abcissa)
    plt.title(titulo)
    plt.show()

def paralista(al):
    l=[]
    l.append("Médias")
    alu = list(al.items())
    for i in alu:
        l.append(i[1])
    return l
def paralistag(al):
    l=[]
    l.append("Grau")
    alu = list(al.items())
    for i in alu:
        l.append(i[1])
    return l


def listadelinhas(): #para meter dataset em lista
    data = []
    with open("alunos.csv", "r", encoding="utf8") as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    f.close()
    return data
def listacomp(lst): #adicionar lista da dist aluno/qqcoisa à lista dataset pode ser media ou avaliacao final
    data = listadelinhas()
    for i in range(len(lst)):
        data[i].append(lst[i])
    return data
def addcolumn_1(data): #addcolumn(listacomp(media(alunos)))
    with open("alunos.csv", "w", encoding= "utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    f.close()


def almedia(alunos):
    dic = {"[1,4.99] - E":0, "[5,8.99] - D":0, "[9,12.99] - C":0, "[13,16.99] - B":0, "[17,20] - A":0,}
    for _,_,_,_, _, _, _, media, *_ in alunos:
        med = float(media) #[(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4)]
        if med < 5:
            dic["[1,4.99] - E"] += 1
        elif med < 9:
            dic["[5,8.99] - D"] += 1
        elif med < 13:
            dic["[9,12.99] - C"] += 1
        elif med < 17:
            dic["[13,16.99] - B"] += 1
        elif med < 21:
            dic["[17,20] - A"] += 1
    return dic

def grau(alunos):
    lst2 = []
    med = list(media(alunos).items())
    for x in range (100):
        if med[x][1] < 5:
            lst2.append((ler()[x][1], "E"))
        elif float(med[x][1]) < 9:
            lst2.append((ler()[x][1], "D"))
        elif float(med[x][1]) < 13:
            lst2.append((ler()[x][1], "C"))
        elif float(med[x][1]) < 17:
            lst2.append((ler()[x][1], "B"))
        elif float(med[x][1]) < 21:
            lst2.append((ler()[x][1], "A"))
    dicio = dict(lst2)
    return dicio

def mediacurso(alunos):
    lst1 = []
    for _, _, curso, t,p,c,v, *_ in alunos:
        media = (int(t)+int(p)+int(c)+int(v))/4
        lst1.append((curso, media))
        s = [n for (eb, n) in lst1 if eb == "ENGBIOM"]
        p = [n for (eb, n) in lst1 if eb == "ENGFIS"]
        q = [n for (eb, n) in lst1 if eb == "LEI"]
        r = [n for (eb, n) in lst1 if eb == "LCC"]
        medeb = sum(s)/25
        medef = sum(p)/32
        medlei = sum(q)/23
        medlcc = sum(r)/20
    dici = dict([("ENGBIOM", round(medeb, 2)), ("ENGFIS", round(medef, 2)), ("LEI", round(medlei, 2)), ("LCC", round(medlcc, 2))])
    return dici

def graf(dist, titulo, abcissa, ordenada):
    x = list(dist.keys())
    y = list(dist.values())
    plt.xlabel(abcissa)
    plt.ylabel(ordenada, rotation= 'vertical')
    plt.plot(x,y,color= "red")
    plt.title(titulo)
    plt.show()

def tabela1(): # media/curso
    print(f"{'':19} {'':_^85}")
    print(f"{'':20}|{'ENGBIOM':^20}|{'ENGFIS':^20}|{'LEI':^20}|{'LCC':^20}|")
    print(f"{'':_^105}")
    print(f"|{'Média:':^19}|{list(mediacurso(ler()).values())[0]:^20}|{list(mediacurso(ler()).values())[1]:^20}|{list(mediacurso(ler()).values())[2]:^20}|{list(mediacurso(ler()).values())[3]:^20}|")
    print(f"{'':_^105}")

def tabela2(): #graus
    print(f"{'':14} {'':_^81}")
    print(f"{'':15}|{'A':^15}|{'B':^15}|{'C':^15}|{'D':^15}|{'E':^15}|")
    print(f"{'':_^96}")
    print(f"|{'Alunos:':^14}|{list(almedia(ler()).values())[4]:^15}|{list(almedia(ler()).values())[3]:^15}|{list(almedia(ler()).values())[2]:^15}|{list(almedia(ler()).values())[1]:^15}|{list(almedia(ler()).values())[0]:^15}|")
    print(f"{'':_^96}")

def tabela3(): #aluno/curso
    print(f"{'':19} {'':_^85}")
    print(f"{'':20}|{'ENGBIOM':^20}|{'ENGFIS':^20}|{'LEI':^20}|{'LCC':^20}|")
    print(f"{'':_^105}")
    print(f"|{'Alunos:':^19}|{list(alcurso(ler()).values())[0]:^20}|{list(alcurso(ler()).values())[1]:^20}|{list(alcurso(ler()).values())[2]:^20}|{list(alcurso(ler()).values())[3]:^20}|")
    print(f"{'':_^105}")