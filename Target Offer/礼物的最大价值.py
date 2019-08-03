'''
在一个 m*n 的棋盘中的每一个格都放一个礼物，每个礼物都有一定的价值（价值大于0）可以从棋盘的左上角开始拿各种里的礼物，
并每次向右或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及上面个的礼物，请计算你最多能拿走多少价值的礼物？
'''



'''
策略就是计算第一行的累加和之后，按照第二行的每个累加值之和来更正前一行的值
这样最后取到的，一定是最大路线最大值
'''
class Solution:
    def getMaxValue(self, values, rows, cols):
        if not values or rows <= 0 or cols <= 0:
            return 0
        
        # 构造一个列表，当走到第i行的时候，这个列表已经保存了第i-1行
        # 所能取到礼物最大一行的值(实际所走路线最大值之后的值)
        maxValues = [0]*cols
        
        for i in range(rows):
            for j in range(cols):
                
                left = 0
                up = 0
                
                if i > 0:
                    up = maxValues[j]
                    
                if j > 0:
                    left = maxValues[j-1]
                    
                maxValues[j] = max(left, up) + values[i*rows+j]
        return maxValues[-1]
s = Solution()
a = s.getMaxValue([1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4)
print(a)