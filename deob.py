import keyword as kw
with open("prog.txt") as f:
    # Построчно читаем файл с функцией 
    code=f.readlines()
# Создаем словари для переменных и списков из кода и их новых названий, также создаем счетчики для них
vars={} 
counter1=1
lists={}
counter2=1
# Обрабатываем первую строчку(заголовок функции)
i=code[0].find("(")
j=code[0].find(")")
s0=[i.strip() for i in code[0][i+1:j].split(",")]
for var in s0:
    if var[0]==",":
        var=var[1:]
    if var[-1]==",":
        var=var[:-1]
    vars[var]="a"+str(counter1)
    counter1+=1
    code[0]=code[0].replace(var,vars[var])
code1=[code[0]] # Создаем список строк нового кода
for line in code[1:]: #Обрабатываем тело функции
    tmp=line
    line=[i.strip() for i in line.split()] # каждую строку делим на части(по пробелам)
    i=0 #Проверяем каждую часть на наличие присваивания(>>>a=1) и разделяем ее по первому одиночному знаку равенства на две части(['a', '=1']), и добавляем их в список line
    while i<len(line):
        if line[i].find("=")!=line[i].find("==") and line[i].find("=") not in [0,-1, len(line)-1]:
            p=line[i].split("=")
            line=line[:i]+[p[0],"="+"".join(p[1:])]+line[i+1:]
        i+=1
    del(i)

    for i in range(len(line)): #Обрабатываем каждое слово
        if line[i]=="=": #Если строка состоит из знака равенства, то пропускаем ее
            continue
        if line[i][-1]=="=": #Если последний символ строки-знак равенства, приписываем его в начало следующей строки
            line[i+1]="="+line[i+1] 
            line[i]=line[i][:-1] 
        word=line[i] 
        if kw.iskeyword(word)==0 and (word[::-1] not in list(vars.keys())+list("]\n):")+list(lists.keys()))  and (len(line)-i>1) and ((len(line[i+1])>=1) and(line[i+1][0]=="=" and line[i+1][1]!="=")) :
            #Проверяем, может ли быть данная подстрока вновь объявленной переменной
            w1=[k.strip() for k in word.split(",")] #Разделяем строку, допуская каскадное присваивание(a=b=c=1)
            if line[i+1][1]=="[" and len(w1)==1 and w1[0] not in lists:
                #Если присвоен список и он присвоен в одну переменную и он объявлен впервые
                lists[w1[0]]="R"+str(counter2) #
                counter2+=1
            else:
                for word1 in [k.strip() for k in word.split(",")]: #Обрабатываем переменные аналогично
                    if word1 not in vars:
                        vars[word1]="a"+str(counter1)
                        counter1+=1
    #Заменяем в строке название ранее объявленные переменные
    for var in vars: 
        tmp=tmp.replace(var, vars[var])
    for lst  in lists: 
        tmp=tmp.replace(lst, lists[lst])
    code1.append(tmp)
with open("function.txt","w") as f: 
    print(*code1,file=f,sep="") 
