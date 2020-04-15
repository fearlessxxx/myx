def all_prime_number(n):
    list_original = list(range(n)) #初始化原始列表
    for i in range(2, n): #遍历列表
        if list_original[i] != 0:
            j = i+i
            while j < n:
                list_original[j] = 0 #如果列表中的值不为0，则把大于该值切为其倍数的元素置为0
                j += i
    return [i for i in list_original[2:] if i != 0] #返回原始列表中不为0的数