# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

input_lst = input().split()
string = sorted(input_lst[0])
num = int(input_lst[1])

res = permutations(string, num)

for item in res:
    print(''.join(item))
