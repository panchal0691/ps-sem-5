def luckBalance(k, contests):
    balance = 0
    ls_important = []
    for i in range(n):
        li, ti = contests[i]
        if ti == 0:
            balance += li
        else:
            ls_important.append(li)
    ls_important.sort()
    if len(ls_important)>k:
        for i in range(len(ls_important)-k):
            balance -= ls_important[i]
        for i in range(len(ls_important)-k, len(ls_important)):
            balance += ls_important[i]
    elif len(ls_important)<=k:
        for i in range(len(ls_important)):
            balance += ls_important[i]
    return balance
