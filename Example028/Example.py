# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.
def rle(string):
    resultString = ""
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count = count + 1
            i = i + 1
        if count == 1:
            resultString += string[i]
        else:
            resultString += string[i] + str(count)
        i = i + 1
    return resultString


s = input("Введите строку: ")
valid = set('QWERTYUIOPASDFGHJKLZXCVBNM')
if (set(s).issubset(valid)):
    print(rle(s))
else:
    print("ОШИБКА: Не валидная строка")