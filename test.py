day = ['a', 'b', 'c', 'c', 'a', 'd']
day_new = []
for a in day:
    if a not in day_new:
        day_new.append(a)
print(day_new)
