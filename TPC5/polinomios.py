polinomio1 = [(1,1)]
polinomio2 = [(2,1), (1,0)]
polinomio3 = [(7,5), (6,3), (-2,2), (27,0)]

def criaPolIn():
    g = int(input("Grau do polinómio"))
    lst = []
    while g >= 0:
        c = int(input("Coeficiente do termo de grau:" + str(g)))
        lst.append((c,g))
        g = g - 1
    return lst

def pot(p,x):
    res = 1
    while x>0:
        res = p * res
        x = x-1
    return res
def calpol(l, z):
    sum = 0
    for termo in l:
        c,g = termo
        sum = c*pot(z, g) + sum
    return sum

def verPolinomio(p):
    for m in p:
        c, g = m
        if g != 0:
            if c > 0:
                print(" + " + str(c) + "x^" + str(g), end="")
            elif c < 0:
                print(" " + str(c) + "x^" + str(g), end="")
        else:
            print(" + " + str(c))
    return

def grauPolinomio(p):
    maior = 0
    for term in p:
        for grau in term:
            coef, grau = term
            if grau > maior:
                maior = grau
    return maior

def tabela(p, linhas):
    i = 0
    while i < linhas:
        print(i, "|", calpol(p,i))
        i = i + 1
    return

def derivarPolinomio(p):
    newlst = []
    for term in p:
        coef, grau = term
        if grau != 0 and coef != 0:
            newc = coef*grau
            newg = grau - 1
            newlst.append((newc,newg))
    return newlst

def guardarPolinomio(p, fnome):
    file = open(fnome, "w")
    for pol in p:
        for termo in pol:
            c,g = termo
            file.write(str(c) + ";" + str(g))
            file.write(" @ ")
        file.write("\n")
    file.close()
    return
    
def recuperarPolinomio(fnome):
    file2 = open(fnome, "r")
    biglst = []
    for line in file2:
        lst = []
        termos = line.split("@")
        for t in termos:
            elems = t.split(";")
            if len(elems)==2:
                coe=elems[0]
                grau = elems[1]
                term = (coe, grau)
                lst.append(term)
        biglst.append(lst)
    return biglst

