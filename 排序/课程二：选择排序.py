# alist=[54,226,93,17,77,31,44,55,20]
# alist=[17,226,93,54,77,31,44,55,20]
# alist=[17,20,93,54,77,31,44,55,226]

# j=0
# min=0  从alist[0]与alist[0+1]开始进行对比
# 即从alist[j]与alist[j+1]开始对比
# alist[0],alist[3]=alist[3],alist[0]

# j=1
# min=1
# alist[1],alist[8]=alist[8],alist[1]

#

# 从无序列表中选择一位为最小值
# 后用最小值与第一位进行更换位置
# 再从后面的无序列表中在招最小值，与第二位进行更换位置
# 从无序序列中找到最小值，再替换到有序列表中

def select_sort(alist):
    '''选择排序'''
    n = len(alist)
    for j in range(0, n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        # 找到min_index最小值时退出循环进行交换
        alist[min_index], alist[j] = alist[j], alist[min_index]
    return alist

# i=0~n-1 range(0,n-1-0) j=0
# i=1~n-2 range(0,n-1-1) j=1
# j=n range(0,n-1-j)


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(select_sort(alist))


# 最坏时间复杂度O（n^2）
# 最优时间复杂度O（n^2）
# 不稳定