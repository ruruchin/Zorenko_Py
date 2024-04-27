""". В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
текстовый файл все даты февраля в формате ДД/ММ/ГГГГ."""
import re
bom = re.compile(r"\d{2}\.\d{2}\.\d{4}")
bim = re.compile(r"\d{2}[/]\d{2}[/]\d{4}")

with open("dates.txt", 'r') as file:
    reding = file.read()
for _ in range(len(reding)):
    l = bom.findall(reding)
    s = bim.findall(reding)
kolVoL= len(l)
kolVoS= len(s)

file2 =open("datas_final.txt","w")
file2.writelines('\n'.join(s))
print(l)
print(s)
print(f'Количество дат в формате: ДД.ММ.ГГГГ {kolVoL}')
print(f"Количество дат в формате: ДД/ММ/ГГГГ {kolVoS}")





