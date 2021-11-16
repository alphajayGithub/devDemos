## set 不重复元素集
def is_duplicated(lst):
    for x in lst:
        if lst.count(x) >1:
            return True
    return False

def is_duplicated2(lst):
    print("len is", len(lst))
    print(set(lst))

    return len(lst) != len(set(lst))


a = [1, -2, 3, 4, 1, 2]


print(is_duplicated(a))
print(is_duplicated2(a))


## set的用法
x = set('runoob')
y = set('google')
print(x, y)        # 去重
print(x&y)         # 交集
print(x|y)         # 并集
print(x-y)         # 差集