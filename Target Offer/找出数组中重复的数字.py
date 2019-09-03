'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''

# -*- coding:utf-8 -*-
def repeatable_num(a):
    if a == []:
        return "请输入含有具体数值的数组"
    
    repeat_num = []
    
    for i in range(len(a)):
        # 比较第i个数字是否和下标对应
        if i != a[i]:
            # 如果a[i]和a[i]下标对应的数字相等，就重复了
            if a[i] == a[a[i]]:
                repeat_num.append(a[i])
            # 把a[i]的值放在他应用的下标的位置，就是做替换
            else:
                a[i], a[a[i]] = a[a[i]], a[i]

    return repeat_num
