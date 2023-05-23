import random
n = input('Vvedite slovo')
d = 'ф'
x = 1
i = 1
print(len(n))
while i <= len(n):
    n = n[:(len(n)-1)]
    s = n[1:]
    if s == d:
       x = 1

if x == 0:
    print('Ого! Это редкое слово!')
else:
    print('Эх! Слово, конечно, не редкость!')



