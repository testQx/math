'''
算法是否稳定
例如 (1,2) (3,1) (3,7) (4,5) 根据元组中第一个数字来进行排序
若结果一直为 (1,2) (3,1) (3,7) (4,5) ，称为稳定算法
若结果不稳定，称为不稳定算法 (1,2) (3,1) (3,7) (4,5) 或者  (1,2) (3,7) (3,1) (4,5)
'''


def bubble_sort(alist):
    '''冒泡排序，使用顺序表'''
    n = len(alist)
    for j in range(n - 1):
        # 外层班长需要走多少次，n-1次，从0开始，最后一位自动排序不需要再走
        count = 0
        # 代表交换次数
        for i in range(0, n - 1 - j):
            # 班长从头走到尾
            # 因为下标是从0开始，最后一个数为alist[n-1]
            # 从alist[0]一直到alist[n-2]，最后一个数不需要再比较，比较到倒数第二个数即可，所以范围为（0,n-1）
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            return alist
    return alist


#  i 0 ~n-2  range(0,n-1-0)  j=0
#  i 0~ n-3  range(0,n-1-1)  j=1
#  i 0~ n-4  range(0,n-1-2)  j=2
#  j=n range(0,n-1-j)


if __name__ == '__main__':
    li = [123, 32, 542, 5756, 53, 234, 543]
    print(bubble_sort(li))
# 最坏时间复杂度O（n^2）
# 最优时间复杂度O（n）
# 稳定