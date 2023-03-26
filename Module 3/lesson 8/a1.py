def get_avg_lists(lst1, lst2):
    summ = []
    for i in lst1:
        for j in lst2:
            if i == j and type(i) in (int, float):
                summ.append(i)

    if len(summ) == 0:
        return 0
    else:
        return sum(summ) / len(summ)
