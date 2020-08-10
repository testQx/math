# alist=[54,26,93,17,77,31,44,55]
# 先进行对半拆分
# 54，26，93，17    77，31，44，55
# 54，26   93，17   77，31   44，55
# 54  26   93 17 77 31 44 55
# 后进行两两合并
# 26，56   17，93  31，77 44，55
# 后引入指针
# 例如26，55    17，93
#   left      right
# 然后left与right进行对比排序

def merge_sort(alist):
    '''归并排序'''
    # 先写拆分，使用递归
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left 采用归并排序后形成的有序的新的列表
    left_alist = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_alist = merge_sort(alist[mid:])
    # merge(left_alist,right_alist)
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_alist) and right_pointer < len(right_alist):
        if left_alist[left_pointer] <= right_alist[right_pointer]:
            result.append(left_alist[left_pointer])
            left_pointer += 1
        else:
            result.append(right_alist[right_pointer])
            right_pointer += 1
        # 操作合并
        result += left_alist[left_pointer:]
        result += right_alist[right_pointer:]
        return result


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(alist))

    # merge_sort([54,26,93,17])
    # merge_sort([54,26])
    # merge_sort([54])->return alist 即返回了54
    # 然后再次往回读merge_sort([54,26])-> left_alist=return [54]
    #                                    right_alist = merge_sort([54,26][1:])-> merge_sort([26])->right_alist=return [54]
    #                                    然后继续往下执行合并返回result为[54,26]

# 最坏时间复杂度O(nlogn)
# 最优时间复杂度O(nlogn)
# 稳定
# 会产生新的列表，速度最快
