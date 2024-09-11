import math

def solution(r1, r2):
    answer = 0
    line_spot = (r2 - r1 + 1) * 4
    
    r_tot_num = 0
    for i in range(1, r2):
        if (r1 > i):
            r1_point = math.ceil(math.sqrt(r1**2 - i**2))
        else:
            r1_point = 1
        r2_point = math.floor(math.sqrt(r2**2 - i ** 2))
        r_tot_num += (r2_point - r1_point + 1)
            
    return (r_tot_num) * 4 + line_spot

def solution_timeout(r1, r2): #시간초과 n = 1,000,000 -> nlogn 이하의 alg가 필요
    line_spot = (r2 - r1 + 1) * 4
    
    r_tot_num = 0
    for i in range(1, r2 + 1):
        for j in range(1, r2 + 1):
            if pow(r1, 2) <= pow(i , 2) + pow (j , 2) <= pow(r2, 2):
                r_tot_num += 1
            
    return (r_tot_num) * 4 + line_spot


def solution_fail(r1, r2):
    answer = 0
    line_spot = (r2 - r1 + 1) * 4
    diagonal_num = 0
    r2_tot_num = 0
    
    for i in range(1, r2):
        if i >= r2 - i:
            continue
        if pow(i , 2) + pow (r2 - i , 2) <= pow(r2, 2):
            r2_tot_num += 1
    for i in range(1, r2):
        if pow(r1, 2) <= pow(i , 2) + pow (i , 2) <= pow(r2, 2):
            diagonal_num += 1
    r2_tot_num *= 2
    diagonal_num *= 4
    
    r1_tot_num = 0
    for i in range(1, r1):
        if i >= r1 - i:
            continue
        if pow(i , 2) + pow (r1 - i , 2) < pow(r1, 2):
            r1_tot_num += 1
    r1_tot_num *= 2 
    
    return (r2_tot_num - r1_tot_num) * 4 + line_spot + diagonal_num