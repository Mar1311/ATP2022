import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def quad(a,b,l):
    x = [l,l,-l,-l,l]
    y = [l,-l,-l,l,l]
    plt.plot(x, y)
    eixoXx = [-l,l]
    eixoXy = [a,b]
    plt.plot(eixoXx, eixoXy, color='white', linewidth = 0.01)
    eixoYx = [b,a]
    eixoYy = [-l,l]
    plt.plot(eixoYx, eixoYy, color='white', linewidth = 0.01)
    plt.show()

def nquad(e,f,o):
    for l in o:
        x = [l,l,-l,-l,l]
        y = [l,-l,-l,l,l]
        plt.plot(x, y)
    i = max(o)
    eixoXx = [-i,i]
    eixoXy = [e,f]
    plt.plot(eixoXx, eixoXy, color = 'None')
    eixoYx = [f,e]
    eixoYy = [-i,i]
    plt.plot(eixoYx, eixoYy, color= 'None')
    plt.show()

def rect(c,v,l,a):
    plt.axes()
    x = [l,l,-l,-l,l]
    y = [a,-a,-a,a,a]
    plt.plot(x,y)
    s = l+1
    t = a+1
    eixoXx = [-s,s]
    eixoXy = [c,v]
    plt.plot(eixoXx, eixoXy, color = "None")
    eixoYx = [v,c]
    eixoYy = [-t,t]
    plt.plot(eixoYx, eixoYy, color= "None")
    plt.show()

def nrect(r):
    count = 0
    i = 1
    while i<r+1:
        if i%2!=0:
            rect=mpatches.Rectangle((count, 0), 20, 100, fill = False, color = "red")
            plt.gca().add_patch(rect)
            count += 22
            i += 1
        else:
            rect2 = mpatches.Rectangle((count, 0), 10,70, fill = False, color= "yellow")
            plt.gca().add_patch(rect2)
            count += 12
            i += 1
    eixoXx = [0, count]
    eixoXy = [0,0]
    plt.plot(eixoXx, eixoXy, color = "None")
    eixoYx = [0,0]
    eixoYy = [0,100]
    plt.plot(eixoYx, eixoYy, color= "None")
    plt.show()
#lado a lado, em que os ímpares têm altura 100 e largura 20 e os pares altura 70 e largura 10

def circ(a,b,r):
    plt.axes()
    circulo = plt.Circle((a,b),r, fc='blue',ec="green", linewidth = 3)
    plt.gca().add_patch(circulo)
    plt.axis('scaled')
    plt.show()

def ncirc(c,d,rr):
    plt.axes()
    lst = list(rr)
    lst.sort(reverse=True)
    for i in lst:
        circu = plt.Circle((c,d), i, fc = "yellow", ec="red", linewidth = 3)
        plt.gca().add_patch(circu)
    plt.axis("scaled")
    plt.show()


