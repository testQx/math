# alist=[54,26,93,17,77,31,44,55,20]
#           low                  high
# 当low指针向右走，对应数若大于54，则停下
# high指针向左走，对应数若小于54，则停下
# 此时讲hgih与Low的值交换后；继续走
# 直到low与high重合，代表找到54存放位置；左边均小于54，右边均大于54
# 当54排序好后，分为两个部分继续执行，[26,20,17,44,31] 和[77,55,93]


def quick_sort(alist, first, last):
    if first >= last:
        return alist
    low = first
    high = last
    mid_value = alist[first]
    # 代表列表只有一个元素
    while low < high:
        # 这里的low<high是控制先右走再左走，交替执行
        # 特殊情况：当有数值与mid_value相等时，需要把等于放到其中一边
        while low < high and alist[high] >= mid_value:
            # 这里的low<high是控制继续向左走
            # 当满足条件时 继续走
            # 不满足条件时，外部替换
            high -= 1
        alist[low] = alist[high]
        # low+=1
        while low < high and alist[low] < mid_value:
            # 这里的low<high是控制继续向右走
            low += 1
        alist[high] = alist[low]
        # high+=1
    # 从循环退出时，low=high
    alist[low] = mid_value
    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low - 1)
    # 对low右边的列表执行快速排序
    quick_sort(alist, low + 1, last)
    return alist
    # quick_sort(alist[:low-1])
    # quick_sort(alist[low + 1:])
    # 切片后再操作是形成一个新列表
    # 需要对同一个列表进行操作


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(alist, 0, len(alist) - 1))

# 最坏时间复杂度O(n^2)
# 最优时间复杂度O(logn)
# 不稳定
