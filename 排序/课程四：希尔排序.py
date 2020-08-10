# alist=[54,26,93,17,77,31,44,55,20]
# 假设当gap=4时，取间隔
#        54          77          20 为一个无序序列  -> 20  54 77
#           26          31                        -> 26  31
#             93           44                     -> 44 93
#                17          55                   -> 17 55
# 后进行插入排序互换位置
# alist=[20,26.44.17.54.31,93,55,77]
# 后再次取gap=2，取间隔，直至间隔取至为1，排序完成
def shell_sort(alist):
    '''希尔排序'''
    '''在插入算法上进行'''
    n = len(alist)
    gap = n // 2  # 9/2取4
    # gap变化到0之前，插入算法的执行次数 1//2==0
    while gap > 0:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


if __name__ == '__main__':
    alist = [93, 54, 77, 31, 44, 55, 226]
    print(shell_sort(alist))

# 最坏时间复杂度O（n^2）
# 最优时间复杂度不稳定，根据步长决定
# 不稳定
