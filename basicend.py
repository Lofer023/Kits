"""
Дана строка. Посчитай, сколько в ней гласных букв.
Разверни список «вручную» (без [::-1]).
Удали дубликаты из списка чисел, сохранив порядок.
"""
def strandmass1(text):
    bas = "aeiouy"
    text  = text.lower()
    i = 0
    for j in text:
       if j in bas:
            i+=1
    return i

print(strandmass1('abracadabra'))

def strandmass2(spisok):
   mass = []
   for _ in range(len(spisok)-1,-1,-1):
      mass.append(spisok[_])
   return mass

print(strandmass2([2,1,8,7,6,9,12,3,5]))

def strandmass3(spisok):
   mass = []
   ss = set()
   for i in spisok:
       if i not in ss:
        ss.add(i)
        mass.append(i)
       else: 
        continue
   return mass
#
print(strandmass3([2,2,8,7,2,9,3,3,5]))