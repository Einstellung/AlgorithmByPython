'''
在一个数组中除一个数字只出现一次之外，
其他数字都出现了三次。请找出那个只出现一次的数字
'''


'''
这个问题的核心思路是如果一个二进制出现三次，那么它的二进制表示的每一位（0或者1）也出现
三次，如果把所有出现三次的数字二进制表示的每一位都分别加起来，那么每一位的和都能被3整除
'''

class Solution:
    def FindNumberAppearingOnce(self, array):
        if array == None or len(array) <= 0:
            return []
        
        # 用来存放整形的32个位置
        bitSum = [0]*32
        
        for i in range(len(array)):
            bitMask = 1
            
            # 一定要注意j的顺序，，判断最小的数在末尾向前走，
            # 否则最后result二进制转化为十进制会出错
            for j in range(31, -1, -1):
                # 判断最后一位是否为1，等bitMask向前移动一位之后
                # 就在判断前一位是否为1了
                bit = array[i] & bitMask
                # 当为1的时候，对应位置就加1
                if bit != 0:
                    bitSum[j] += 1
                bitMask = bitMask << 1

        result = 0
        for i in range(32):
            # 这里bitSum数的顺序又是从前向后了
            # 因此result要数一次左移动一次，但是左移运算
            # 不能放在加的后面，否则就会多左移（二进制个位左移变成十位了）一个
            result = result << 1
            result += bitSum[i] % 3
            
        return result

a = Solution()
array = [1, 2, 2, 2, 3, 3, 3]
a.FindNumberAppearingOnce(array)