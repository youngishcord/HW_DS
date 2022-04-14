import numpy as np
import sys

def arr1(n):
    return np.arange(n-1,-1,-1)

#print(arr1(int(input('Введите число '))))

def diag_matrix(n):
    return np.diag(np.arange(n-1,-1,-1)), f"сумма элементов на диагонали = {sum(np.diag(np.diag(np.arange(n-1,-1,-1))) )}"

#print(diag_matrix(int(input("Введите число "))))

def solve_sys():
    a = int(input('введите кол-во неизвестных '))
    q = np.zeros((a,a))
    w = np.zeros((a,1))
    for i in range(a):
        for j in range(a+1):
            if j == a:
                w[i][0] = int(input(" = "))
                continue
            q[i][j] = int(input(f"X{j+1} * "))
        print(f'уравнение: ',end = '')
        for k in range(a+1):
            if k == a:
                print(f' = {w[i][0]}')
                continue
            print(f'+({q[i][k]}*X{k+1})',end='')

    ans = np.linalg.solve(q,w)
    for i in range(a):
        print(f"X{i+1}", ans[i][0])
    return np.linalg.solve(q,w)

#solve_sys()


import numpy as np
users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ], 
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

def angle(stats, user):
    a = np.linalg.norm(stats)
    b = np.linalg.norm(user)
    return np.arccos(np.dot(stats, user)/(a*b))*360/2/np.pi


def same_user(users_stats, user):
    min_angle = sys.maxsize
    for i in range(len(users_stats)):
        m = angle(users_stats[i], user)
        #print(m)
        #print('\n')
        if m < min_angle:
            min_angle = m
            uid = i+1
    return uid



#print(same_user(users_stats, next_user_stats))