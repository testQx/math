# 类比于翻字典，例如要找P字母
# 随机翻开一页，结果是C，则向后找，C前面部分不管。再翻开，如果是R，则再向前找，R后面的部分不管

# 二分法查找/折半查找，必须建立在有序顺序表上，需要支持索引，则链表不支持
def binary_search(alist, item):
    '''二分查找,递归'''
    n = len(alist)
    if n > 0:
        mid = n // 2
        # 代表中间值
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False


def binary_search_not(alist, item):
    '''二分查找,非递归'''
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    alist = [31, 44, 54, 55, 77, 93, 226]
    print(binary_search(alist, 77))
    print(binary_search(alist, 74))
    print(binary_search_not(alist, 77))
    print(binary_search_not(alist, 74))
# 最坏时间复杂度O(logn)
# 最优时间复杂度O(1)
