#!/usr/bin/env python3

import re, argparse

def alignment_cost(seq1,seq2):
    m = len(seq1)
    n = len(seq2)

    c = [[0] * (n+1) for i in range(m+1)]
    b = [[0] * n for i in range(m)]

    for i in range(m+1):
        c[i][0] = i
    for j in range(n+1):
        c[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if seq1[i-1] == seq2[j-1]:
                c[i][j] = c[i-1][j-1]
                b[i-1][j-1] = 'top-left'
            else:
                if (c[i-1][j] > c[i-1][j-1]) & (c[i][j-1] > c[i-1][j-1]):
                    c[i][j] = c[i-1][j-1] + 1
                    b[i-1][j-1] = 'top-left'
                else:
                    if c[i-1][j] > c[i][j-1]:
                        c[i][j] = c[i][j-1] + 1
                        b[i-1][j-1] = 'left'
                    else:
                        c[i][j] = c[i-1][j] + 1
                        b[i-1][j-1] = 'up'

    print('The optimal cost is {}'.format(c[-1][-1]))
    output_file = []
    output_file.append('The optimal cost is {}'.format(c[-1][-1]))

    new_seq1 = []
    new_seq2 = []
    i = m
    j = n
    while i and j:
        if b[i-1][j-1] == 'top-left':
            new_seq1.append(seq1[i-1])
            new_seq2.append(seq2[j-1])
            i = i-1
            j = j-1
        elif b[i-1][j-1] == 'up':
            new_seq1.append(seq1[i-1])
            new_seq2.append('-')
            i = i-1
        else:
            new_seq1.append('-')
            new_seq2.append(seq2[j-1])
            j = j-1

    new_seq1.reverse()
    new_seq2.reverse()
    print('One optimal alignment is :')
    print(''.join(new_seq1))
    print(''.join(new_seq2))
    for i in c:
        print(i)
    output_file.append('One optimal alignment is :')
    output_file.append(''.join(new_seq1))
    output_file.append(''.join(new_seq2))
    

    return output_file

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='This is a script for DPAlignment.')
    # parser.add_argument('inputfile_1', help='Input fisrt of two input files')
    # parser.add_argument('inputfile_2', help='Input second of two input files')
    # parser.add_argument('-o','--output',help='Output file name and location',
    #                     required=True)
    # args = parser.parse_args()
    with open('inputfile_1') as file1:
        sequence_1 = file1.read()
        sequence_1 = re.sub(r'\s','',sequence_1)
    with open('inputfile_2') as file2:
        sequence_2 = file2.read()
        sequence_2 = re.sub(r'\s','',sequence_2)
    with open('output','w') as output:
        output.write(' \n'.join(alignment_cost(sequence_1, sequence_2)))    
    


    
