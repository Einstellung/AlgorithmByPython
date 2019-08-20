def merge_sort( li ):
    # 不断递归调用自己一直到拆分成单个元素的时候就返回这个元素，不再拆分了
    if len(li) == 1:
        return li

    #取拆分的中间位置
    mid = len(li) // 2
    #拆分过后左右两侧子串
    left = li[:mid]
    right = li[mid:]

    # 对拆分过后的左右再拆分 一直到只有一个元素为止
    # 最后一次递归时候ll和r1都会接到一个元素的列表
    # 最后一次递归之前的ll和rl会接收到排好序的子序列
    ll = merge_sort( left )
    rl = merge_sort( right )

    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
    return merge(ll , rl)

#这里接收两个列表
def merge( left , right ):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left)>0 and len(right)>0 :
        #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append( left.pop(0) )
        else:
            result.append( right.pop(0) )
    # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result

if __name__ == '__main__':
    li = [5,4 ,3 ,2 ,1]
    li2 = merge_sort(li)
    print(li2)