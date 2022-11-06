import TPC7 as t
menu = (
    "\n----xxx----\nESCOLHA UMA OPÇÃO\n"
    "1 - Informação do ficheiro\n"
    "2 - Distribuição de alunos por curso\n"
    "3 - Média dos tpc's 1,2,3 e 4 (coluna acrescentada ao dataset)\n"
    "4 - Média por escalões A,B,C,D e E (coluna acrescentada ao dataset)\n"
    "5 - Informação do ficheiro com as novas colunas\n"
    "6 - Distribuições em gráficos de barras\n"
    "7 - Distribuições em gráficos de linhas\n"
    "8 - Distribuições em tabela\n"
    "0 - Sair\n"
)
user = 10
alunos = t.ler()
while user != 0:
    print(menu)
    user = int(input("Qual a opção do menu?"))
    print("--> Opção selecionada:", user, "\n")
    if user == 1:
        print(f"{'Informação do ficheiro':-^61}")
        print(f"|{'id':^5}|{'nome':^12}|{'curso':^12}|{'TPC1':^6}|{'TPC2':^6}|{'TPC3':^6}|{'TPC4':^6}|")
        for x in range(100):
            print(f"|{t.ler()[x][0]:^5}|{t.ler()[x][1][:10]:^12}|{t.ler()[x][2]:^12}|{t.ler()[x][3]:^6}|{t.ler()[x][4]:^6}|{t.ler()[x][5]:^6}|{t.ler()[x][6]:^6}|")

    elif user == 2:
        print(f"{'Distribuição de alunos por curso':-^51}")
        print(t.alcurso(alunos))
        print(f"{'':-^51}")
        print(f"|{'LEI':^11}|{'ENGFIS':^12}|{'LCC':^11}|{'ENGBIOM':^12}|")
        lst = list(t.alcurso(alunos).values())
        print(f"|{lst[0]:^11}|{lst[1]:^12}|{lst[2]:^11}|{lst[3]:^12}|")
        
    
    elif user == 3:
        print(f"{'Média dos TPCs por alunos':-^50}")
        print(f"|{'Aluno':^40}|{'Média':^7}|")
        al = list(t.media(alunos).items())
        for x in range(100):
            print(f"|{al[x][0][:38]:^40}|{al[x][1]:^7}|")
        # adicionar no csv
        t.addcolumn_1(t.listacomp(t.paralista(t.media(alunos))))
    
    elif user == 4:
        print(f"{'Escalão de cada aluno':-^52}")
        print(f"|{'Aluno':^40}|{'Escalão':^9}|")
        al = list(t.grau(t.ler()).items())
        for x in range(100):
            print(f"|{al[x][0][:38]:^40}|{al[x][1]:^9}|")
        # adicionar no csv
        t.addcolumn_1(t.listacomp(t.paralistag(t.grau(alunos))))

    elif user == 5:
        print(f"{'Informação do novo ficheiro':-^75}")
        print(f"|{'id':^5}|{'nome':^12}|{'curso':^12}|{'TPC1':^6}|{'TPC2':^6}|{'TPC3':^6}|{'TPC4':^6}|{'Média':6}|{'Grau':6}")
        for x in range(100):
            print(f"|{t.ler()[x][0]:^5}|{t.ler()[x][1][:10]:^12}|{t.ler()[x][2]:^12}|{t.ler()[x][3]:^6}|{t.ler()[x][4]:^6}|{t.ler()[x][5]:^6}|{t.ler()[x][6]:^6}|{t.ler()[x][7]:^6}|{t.ler()[x][8]:^6}|")

    elif user == 6:
        l = 4
        while l != 0:
            print("1 - Distribuição de alunos por curso\n"
        "2 - Distribuição de alunos por escalão\n"
        "3 - Distribuição da média de cada curso\n"
        "0 - Sair")
            l = int(input("Qual a distribuição que pretende ver?"))
            if l == 1:
                print("\nGráfico de barras:\n")
                print(t.distribuicaoP(t.alcurso(t.ler()), "Distribuição dos alunos por curso", "Curso", "Número de alunos"))
            if l == 2:
                print("\nGráfico de barras:\n")
                print(t.distribuicaoP(t.almedia(t.ler()), "Distribuição dos alunos por Escalão", "Escalões", "Número de alunos"))
            if l == 3:
                print("\nGráfico de barras:\n")
                print(t.distribuicaoP(t.mediacurso(t.ler()), "Distribuição da média por cada curso", "Curso", "Média"))
        if l == 0:
            print("Saiu da opção 6")
    
    elif user == 7:
        o = 4 #dist, titulo, abcissa, ordenada
        while o != 0:
            print("1 - Distribuição de alunos por curso\n"
        "2 - Distribuição de alunos por escalão\n"
        "3 - Distribuição da média de cada curso\n"
        "0 - Sair")
            o = int(input("Qual a distribuição que pretende ver?"))
            if o == 1:
                print("\nGráfico de linha:\n")
                print(t.graf(t.alcurso(t.ler()), "Distribuição dos alunos por curso", "Curso", "Número de alunos"))
            if o == 2:
                print("\nGráfico de linha:\n")
                print(t.graf(t.almedia(t.ler()), "Distribuição dos alunos por Escalão", "Escalões", "Número de alunos"))
            if o == 3:
                print("\nGráfico de linha:\n")
                print(t.graf(t.mediacurso(t.ler()), "Distribuição da média por cada curso", "Curso", "Média"))
        if o == 0:
            print("Saiu da opção 6")
    
    elif user == 8:
        m = 5
        while m != 0:
            print("1 - Tabela de alunos por curso\n"
            "2 - Tabela de alunos por escalão\n"
            "3 - Tabela da média de cada curso\n"
            "0 - Sair")
            m = int(input("Qual a Tabela que pretende ver?"))
            if m == 1:
                print(f"{'Tabela de alunos por curso':_^105}")
                print(t.tabela3())
            if m == 2:
                print(f"{'Tabela de alunos por Escalão':_^96}")
                print(t.tabela2())
            if m == 3:
                print(f"{'Tabela da média de cada curso':_^96}")
                print(t.tabela2())

    elif user > 9:
        print("Opção não existe, tente novamente")

if user == 0:
    print(f"{'Saiu da aplicação':-^110}\n{'':-^110}")