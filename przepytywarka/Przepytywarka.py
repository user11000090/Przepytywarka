print("PRZEPYTYWARKA")
state=""
while state!="exit":
    state=""
    dostepne_zestawy=[]
    zest=open("zestawy.txt","r+", encoding="utf-8")
    loaded_sets=zest.read().split("\n")
    dostepne_zestawy.extend(loaded_sets)
    print("dostępne zestawy pytań:", *dostepne_zestawy)
    zadania = input("wybierz zestaw lub stwórz nowy:\n")
    zestaw = "zadania_{}.txt".format(zadania)
    qa_list = []
    qep=0
    repeat=False
    randm=True
    qe=0
    a=""
    try:
        file = open(zestaw, "r", encoding="utf-8")
    except IOError:
        file = open(zestaw, "w+", encoding = "utf-8")
        dostepne_zestawy.append(zadania)
        zest.write(zadania+"\n")
    loaded = file.read().split("\n")
    qa_list.extend(loaded)
    qa_list.pop()
    print("aby wyświetlić wszystkie pytania i odpowiedzi wybranego zestawu, wpisz \"all\"\naby edytować zadanie, wpisz jego numer\naby zakończyć tryb edycji i rozpocząć przepytywanie, wpisz \"start\"")

    while True:
        qa_temp = []
        pyt=str(input("podaj treść nowego pytania lub numer istniejącego:\n"))
        if pyt == "start":
            break
        elif pyt == "remove":
            qa_list.pop()
            qa_list.pop()
            print("poprzednie zadanie wraz z odpowiedzią zostały usunięte")
            continue
        elif pyt=="all":
            for a in range(len(qa_list)):
                if a==0 or a%2==0: print("pytanie "+str(int((a+2)/2))+": " + qa_list[a])
                else: print("odpowiedź "+str(int(((a-1)+2)/2))+ ": " + qa_list[a])
            continue
            print("aby edytować zadanie, wpisz jego numer\naby zakończyć tryb edycji i rozpocząć przepytywanie, wpisz \"start\"\n")
        try:
            if int(pyt)<=len(qa_list)/2:
                qa_list[(int(pyt)-1)*2]=str(input("podaj nową treść pytania nr {}: ".format(pyt)))
                qa_list[(int(pyt)-1)*2+1]=str(input("podaj nową odpowiedź na pytanie nr {}: ".format(pyt)))
            continue
        except ValueError:
            pass
        odp=str(input("podaj odpowiedź:\n"))
        if odp == "start":
            qa_temp.clear()
            break
        elif odp == "remove":
            qa_list.pop()
            qa_list.pop()
            qa_temp.clear()
            print("ostatnie zadanie wraz z odpowiedzią zostały usunięte")
            continue
        elif odp=="all":
            for a in range(len(qa_list)):
                if a==0 or a%2==0: print("pytanie "+str(int((a+2)/2))+": " + qa_list[a])
                else: print("odpowiedź "+str(int(((a-1)+2)/2))+": " + qa_list[a])
            continue
            print("aby edytować zadanie, wpisz jego numer\naby zakończyć tryb edycji i rozpocząć przepytywanie, wpisz \"start\"\n")

        qa_temp.append(pyt+" ")
        qa_temp.append(odp)
        qa_list.extend(qa_temp)
    print("aby zobaczyć odpowiedź i przejść do następnego pytania, wpisz \"next\"\naby edytować poprzednie pytanie i odpowiedź, wpisz \"edit\"\naby wyświetlić wszystkie pytania i odpowiedzi, wpisz \"all\"")
    print("aby zmienić tryb przepytywania, wpisz \"order\" lub \"random\" (domyślnie \"random\")\naby zakończyć, wpisz \"quit\"")
    import random

    while True:
        if repeat==False:
            if randm==True:
                qe=random.randrange(int(len(qa_list)/2))
            else:
                if qe>=int(len(qa_list)/2-1):qe=0
                else: qe+=1
        else:qe=qep
        nq = 0
        repeat=False
        while nq == 0:
            a=input("nr {}: ".format(qe+1)+qa_list[qe*2]+"\n")
            try:
                if int(a)>0 and int(a)<=len(qa_list)/2 and a!=qa_list[qe*2+1]:
                    qe=int(a)-1;print("wybrano pytanie nr {}".format(a))
                    continue
                elif (int(a)<=0 or int(a)>len(qa_list)/2) and a!=qa_list[qe*2+1]:
                    qe=0;print("zmieniono pytanie")
                    continue
            except ValueError:
                pass
            if a!=qa_list[qe*2+1]:
                if a=="quit":
                    nq=1
                    break
                elif a == "next":
                    print("odpowiedź:", qa_list[qe*2+1])
                    break
                elif a == "edit":
                    qa_list[qep*2]=str(input("podaj nową treść pytania nr {}:\n".format(qep+1)))+" "
                    qa_list[qep*2+1]=str(input("podaj nową odpowiedź:\n"))
                elif a == "repeat":
                    repeat = True
                    break
                elif a == "order": randm = False; print("włączono tryb \"order\"")
                elif a == "random": randm = True; print ("włączono tryb \"random\"")
                elif a == "all":
                    for a in range(len(qa_list)):
                        if a==0 or a%2==0: print("pytanie "+str(int((a+2)/2))+": " + qa_list[a])
                        else: print("odpowiedź "+str(int(((a-1)+2)/2))+": " + qa_list[a])
                elif a == "answer": print(qa_list[qe*2+1])
                elif a!=qa_list[qe*2+1]:
                    try:
                        if int(a):
                            pass
                    except ValueError: print("spróbuj jeszcze raz")
            elif a==qa_list[qe*2+1]:
                print("dobrze")
                break
        if repeat == False: qep = qe
        if nq == 1:
            break

    s=len(qa_list)
    file = open(zestaw, "w", encoding="utf-8")
    for i in range(s):
        file.write(qa_list[i]+"\n")
    file.close()
    zest.close()
    while state!="main" and state!="exit":
        state=str(input("aby powrócić do ekranu wyboru, wpisz \"main\", aby wyjść z programu, wpisz \"exit\"\n"))
