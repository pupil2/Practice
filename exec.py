filename=input("filename:") # Ввод имени проверяемого файла
with open(filename,"r") as f:
    s=f.read()[:2] # Читаем первые два символа файла
print(s) # Печаем их
print(*[hex(i)[2:] for i in s], sep="") # Печатаем их шестнадцатеричную запись
if s.title()=="MZ": # Проверяем, является ли файл исполняемым
    print("executable, OS Windows")
else:
    print("non-executable")
