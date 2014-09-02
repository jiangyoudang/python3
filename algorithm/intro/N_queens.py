__author__ = 'congliu'



def next_pos(result_list,row_num,n):
    next_list = set(range(n))
    next_list = next_list - set(result_list[:row_num])
    row = 0
    for col in result_list[:row_num]:
        if col+row_num-row <= n:
            next_list -= {col+row_num-row}
        if col+row-row_num >=0:
            next_list -= {col+row-row_num}
        row += 1
    return next_list

def queen(n_row,n,result,Q):  # add queen at n_row
    if n_row == n:
        #print(Q)
        p = Q[:]
        result.append(p)
    for col in next_pos(Q,n_row,n):
        Q[n_row] = col
        queen(n_row+1,n,result,Q)

def solveNQueens(n):
    Q = [0]*n
    result = []
    queen(0,n,result,Q)

    answer = []
    for solution in result:
        curr = []
        for k in solution:
            temp = ['.']*n
            temp[k] = 'Q'
            curr.append(''.join(temp))
        answer.append(curr)
    return answer

print(solveNQueens(4))
# print(result)