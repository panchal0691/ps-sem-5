def icecreamParlor(m, arr):
    cost_dict = {}
    for idx, cost in enumerate(arr):
        req_cost = m - cost
        if req_cost in cost_dict:
            return [cost_dict[req_cost]+1, idx+1]
        cost_dict[cost]=idx
