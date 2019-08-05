'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

class Solution:
    # O(n)的算法, 只有当我们可以修改输入的数组时可用
    # 基于Partition的方法
    def GetLeastNumbers(self, alist, k):
        if alist == None or len(alist) <= 0 or len(alist) < k or k <= 0:
            return []
        
        first = 0
        last = len(alist) - 1
        
        # 获取一次划分，但这个index不一定刚好就是k位置
        # 需要后面逐步缩小范围
        index = self.partition(alist, first, last)
        while index != k - 1:
            if index > k - 1:
                last = index - 1
                index = self.partition(alist, first, last)
            else:
                first = index + 1
                index  = self.partition(alist, first, last)
                
        output = alist[:k]
        return output      
        
    def partition(self, alist, first, last):
        base = alist[first]

        leftmark = first
        rightmark = last

        while leftmark < rightmark:  # 要求左指针必须小于等于右指针，之所以没有等号是因为，在最后一次指针移动的时候就会取等，
                                     # 不满足小于条件的时候其实已经取等了
            if alist[leftmark] <= base:
                leftmark += 1
            if alist[rightmark] >= base:
                rightmark -= 1

            else:      # 当左右指针都停止的时候，交换左右指针所对应的值
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

        # 当左指针和右指针重合的时候，交换右指针对应的值和base对应的值
        alist[rightmark], alist[first] = alist[first], alist[rightmark]

        return rightmark    # rightmark是作为递归排序的标记，所以返回。最后输出alist就是直接排序排好的

        
    # O(nlogk)的算法, 适合海量数据
    # 利用一个k容量的容器存放数组, 构造最大堆, 当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数
    def GetLeastNumbers(self, tinput, k):
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        output = []
        for number in tinput:
            if len(output) < k:
                output.append(number)
            else:
                # 构造最小堆， 不推荐
                # output = heapq.nsmallest(k, output)
                # if number >= output[-1]:
                #     continue
                # else:
                #     output[-1] = number
                # 构造最大堆， 推荐
                output = heapq.nlargest(k, output)
                if number >= output[0]:
                    continue
                else:
                    output[0] = number
        return output[::-1]     # 最小堆用 return output


alist = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.GetLeastNumbers(alist, 4))
