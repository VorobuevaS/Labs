S = ' '
F = ' '
x = 'stop'
while True:
    n = input("Введите слово   ")
    S = S + ' ' + n
    if n == x: break
F = S[:(len(S)-4)]
print(F)