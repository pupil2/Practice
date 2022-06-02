alf="qwertyuiopasdfghjklzxcvbnm_{}1234567890" #алфавит
gamm="thekey" # гамма
text=input() # ввод текста
enctext="" # строка, в которую будет записан зашифрованный текст
k=0 # текущий индекс символа гаммы
for symbol in text: # посимвольный перебор исходного текста
    n=alf.find(symbol) # находим индекс этого символа в алфавите
    if n==-1: # если символа нет в алфавите
        enctext+=symbol #добавляем в ответ текущий символ
    else:
        enctext+=alf[(n+alf.find(gamm[k]))%len(alf)] # шифруем данный символ с помощью шифра Вернама
        k=(k+1)%len(gamm)
print(enctext)
