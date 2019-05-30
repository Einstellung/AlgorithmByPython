'''
给你一根长度为n的绳子，请把绳子剪成m段（m，n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...k[m]。请问k[0]*k[1]*...k[m]可能的
最大乘积是多少？例如，当绳子长度是8时，我们把它剪成长度分别为2、3、3
的三段，此时得到的最大乘积是18
'''

class Solution:
    def maxProductAfterCutting_solution1(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

# 这里的四个数表示的是绳子长度为0，1，2，3时所对应的值，即是最小子绳段数为0，1，2，3不再划分了（当绳子段数大于等于4，可以划分成1,2,3段）。之所以这样写，是4段以上的
# 绳子最小化分对应的就是0，1，2，3。事实上0其实没有什么用，之所以留着0是因为正好是一一对应，比如接下来存储的producsts[4]对应的是第五个数

        products = [0, 1, 2, 3]      
        
        for i in range(4, length+1):
            max_product = 0
            for j in range(1, i // 2 + 1):
                max_product = max(max_product, products[j]*products[i-j])  # 逐个去比较，找出最大值
            products.append(max_product)
        
        return products[-1]

test = Solution()
test.maxProductAfterCutting_solution1(8)