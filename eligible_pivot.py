def eligible_pivot(arr):
    n = len(arr)
    eligible = []
    for i in range(n):
        is_eligible = True
        for j in range(n):
            if i != j and arr[i] >= arr[j]:
                is_eligible = False
                break
        if is_eligible:
            eligible.append(arr[i])
    return eligible
