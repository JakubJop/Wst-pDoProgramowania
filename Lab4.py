
import random
punkty = []
liczba_stud = 15
for i in range(liczba_stud):
    # punkty = random.random() * 100 % 50
    p = random.uniform(0, 50)
    punkty.append(round(p, 2))
print()
print(punkty)
print(f'min = {min(punkty)}')
print(f'max = {max(punkty)}')
p = float(input('Podaj liczbę punktów: '))
if p in punkty:
    print(punkty.index(p))
else:
    print(f'liczba {p} punktów nie występuje na liście')
y = sum(punkty)
sr = round(y/n,2)
print("średnia", sr)
punkty_w = []
punkty_n = []
for i in range[n] :
    if punkty[i]>sr
        punkty_w.append(i)
punkty_n. = ['(p)for p in punkty if p < sr']
print(punkty_w,punkty_n len(punkty_w), len(punkty_n))





