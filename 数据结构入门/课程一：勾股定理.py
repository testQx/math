'''
a+b+c=1000,a2+b2=c2
解法一
枚举法
思路：进行a,b,c=0~1000去试探

import time
start_time=time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c ==1000 and a**2 + b**2 == c**2:
               print(a,b,c)
end_time=time.time()
print(end_time-start_time)

T=1000*1000*1000*1000*2
T（N）=N^3 * 2  只考虑前面的数量级（类似单位），不考虑后方*的具体值
T(N)=N^3 *k =k* g(n) +c 曲线类似
g(N)=N^3
=O(n^3)


#解法二
#思路：已经确定a,b,此时c=1000-a-b
import time
start_time=time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c=1000-a-b
        if  a**2 + b**2 == c**2:
               print(a,b)
end_time=time.time()
print(end_time-start_time)

T（N）=N^2 * (1+ max(1,0))
T(N)=N^2
=O(n^2)
'''


#时间复杂度，表示算法所用时间，速度
#由于每台机器执行的总时间不同，但是执行基本运算数量（步骤）大体相同

#常数项，时间复杂度0（N）=1
#顺序结构：时间复杂度按基本步骤之间的相加计算
#条件（分支）结构：时间复杂度取最大值（看不同分支所需要的步骤数，取最大的一个）
#循环结构：时间复杂度按相乘计算
#其他次要项与常数项去掉
#时间复杂度一般指最坏时间复杂度

#Todo
# 所消耗的时间从小到大
# O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^3)<O(2^n)<O(n!)<O(n^n)


#Python内置类型性能分析
#timeit模块（可用来测试一小段Python代码的执行速度）