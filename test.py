day = ['b', 'a', 'c', 'a', 'c', 'd', 'b']


for a in day:
    print("day", day)
    k = day.count(a)
    print("count", k)
    if k > 1:
        ind = day.index(a)
        print("index", ind)
        day.pop(ind)
    print("kkkkkkkkkkkkkkkkkkk")