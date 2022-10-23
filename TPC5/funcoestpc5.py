import csv

def ler(l):
    with open("myheart.csv", "r") as file:
        reader = csv.DictReader(file)
        lst = []
        for line in reader:
            lst.append(dict(line))
        file.close()
    return lst[l]


def disds():
    with open("myheart.csv", "r") as file:
        reader = csv.reader(file)
        dic = {"Feminino ":0, "Masculino":0}
        lst1f = []       
        lst1m = []        
        for line in reader:
            if line[1] == str("F"):
                if line[5] == str("1"):
                    lst1f.append(1)
                dic.update({"Feminino ": len(lst1f)})
            if line[1] == str("M"):
                if line[5] == str("1"):
                    lst1m.append(1)
                dic.update({"Masculino": len(lst1m)})
        file.close()
    return dic

def ordenar(v):
    return v[0]
def distid(i):
    file = open(i)
    line = csv.reader(file)
    dic2 = {}
    for elem in line:
        if elem[0] in dic2.keys():
            if elem[5] == str("1"):
                dic2[elem[0]] = dic2[elem[0]] + 1
        else:
            if elem[5] == str("1"):
                dic2[elem[0]] = 1
        valores = list(dic2.items())
        valores.sort(key = ordenar)
    s1 = "[30,34]", sum(x[1] for x in valores[0:4])
    s2 = "[35,39]", sum(x[1] for x in valores[4:9])
    s3 = "[40,44]", sum(x[1] for x in valores[9:14])
    s4 = "[45,49]", sum(x[1] for x in valores[14:19])
    s5 = "[50,54]", sum(x[1] for x in valores[19:24])
    s6 = "[55,59]", sum(x[1] for x in valores[24:29])
    s7 = "[60,64]", sum(x[1] for x in valores[29:34])
    s8 = "[65,70]", sum(x[1] for x in valores[34:39])
    s9 = "[70,74]", sum(x[1] for x in valores[39:44])
    s10 = "[75,80]", sum(x[1] for x in valores[44:])
    dicf = dict([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10])
    file.close()
    return dicf

def distcol(i):
    file23 = open(i)
    line = csv.reader(file23)
    dic3 = {}
    for elem in line:
        if elem[3] in dic3.keys():
            if elem[5] == str("1"):
                dic3[elem[3]] = dic3[elem[3]] + 1
        else:
            if elem[5] == str("1"):
                dic3[elem[3]] = 1
    val = list(dic3.items())
    u = sorted([(x[0], x[1]) for x in val])
    a1 = "[0,99]   ", sum(x[1] for x in u[:1])
    a2 = "[100,109]", sum(x[1] for x in u[1:2])
    a3 = "[110,119]", sum(x[1] for x in u[2:5])
    a4 = "[120,129]", sum(x[1] for x in u[5:7])
    a5 = "[130,139]", sum(x[1] for x in u[7:8])
    a6 = "[140,149]", sum(x[1] for x in u[8:10])
    a7 = "[150,159]", sum(x[1] for x in u[10:13])
    a8 = "[160,169]", sum(x[1] for x in u[13:17])
    a9 = "[170,179]", sum(x[1] for x in u[17:24])
    a10 = "[180,189]", sum(x[1] for x in u[24:29])
    a11 = "[190,199]", sum(x[1] for x in u[29:36])
    a12 = "[200,...]", sum(x[1] for x in u[36:])
    dicio = dict([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12])
    file23.close()
    return dicio