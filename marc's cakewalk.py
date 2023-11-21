def marcsCakewalk(calorie):
    sorted_cal = sorted(calorie, reverse=True)
    total_dis = 0
    for index, calories in enumerate(sorted_cal):
        req_dis = calories * (2 ** index)
        total_dis += req_dis
    return total_dis
