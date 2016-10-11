import sys

def num_tasks(total, costs):

    count = 0
    costs = sorted(costs, key=lambda x:(x[0]-x[1],-x[0]))
    for cost in costs:
        if total >= cost[0]:
            count += 1
            total -= cost[0]-cost[1]
        if total <= 0:
            break
    return count

def parse_input():
    N = 0
    T = -1
    F = -1
    costs = []
    res = []
    for line in sys.stdin:

        if T == -1:
            T = int(line)-1
            continue
        if N == 0:
            if F != -1:
                print('cost',costs)
                res.append(num_tasks(F, costs))
                T -= 1
                costs = []
            N, F = line.split()
            N = int(N)
            F = int(F)



        else:
            costs.append(list(map(int, line.split())))
            N -= 1

        if T == 0 and N == 0:
            print('cost',costs)
            res.append(num_tasks(F, costs))
            break
        # print(T, N, F)
    return res
#
# res = parse_input()
# for i in res:
#     print(i)

test = [
    [2,0], [2,0], [4, 2], [6, 4]
]
print(num_tasks(10, test))