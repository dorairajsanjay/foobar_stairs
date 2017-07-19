max = 20
p = a = [[0] * (max+1) for i in range(max+1)]

# adapted from https://github.com/xphoniex/Google-Foobar/blob/master/the_grandest_staircase_of_them_all_answer.java

def fillP():
    p[1][1] = 1
    p[2][2] = 1

    for w in range(3,max+1): 
        for m in range(1,w+1):
            if (w-m == 0):
                p[w][m] = 1 + p[w][m-1]
            elif (w-m < m):
                p[w][m] =  p[w-m][w-m] + p[w][m-1]
            elif (w-m == m):
                p[w][m] = p[m][m-1] + p[w][m-1]
            elif (w-m >m): 
                p[w][m] = p[w-m][m-1] + p[w][m-1]

def answer(n):
    fillP();
    return p[n][n] - 1;

import time
start_time = time.time()
print(answer(20))
end_time = time.time()

print("Elapsed time:",end_time-start_time)
