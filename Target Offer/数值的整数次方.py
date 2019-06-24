'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

'''
需要注意的地方:
当指数为负数的时候
当底数为零切指数为负数的情况
在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内
'''

'''
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度
'''

import math

class Solution:
    def Power(self, base, exponent):
        # 特殊情况，对于底数为0并且指数<0的考虑
        # 对0求倒数并运算会出错
        if math.isclose(base, 0.0) and exponent < 0:
            return 0
        
        result = self.PowerWithUnsignedExponent(base, abs(exponent))
        
        # 如果指数项为0，就将其翻转
        if exponent < 0:
            result = 1 / result
            
        return result
                        
    
    # 定义相应的位运算操作，通过递归来算
    def PowerWithUnsignedExponent(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        
        # 右移运算符作为除法运算
        result = self.PowerWithUnsignedExponent(base, exponent >> 1)
        result *= result
        
        # 查看最后递归到底的exponent是不是奇数1,如果是奇数1就将其变成base
        if(exponent & 0x01 == 1):
            result *= base
            
        return result

S = Solution()
print(S.Power(2, -2))

S = Solution()
print(S.Power(2, 2))