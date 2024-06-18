def change():
    species_lst = [0.01, 0.5, 1, 5, 10, 20, 50, 100]   # 存储各类面额的钱
    species_quantity = list(map(int, input().split()))  # 存储各类面额的钱的数量
    money_total = 0                                    # 表示手头的金额总量
    back_quantity = [0, 0, 0, 0, 0, 0, 0, 0]                  # 表示找回钱币面额的数量
    for i in range(len(species_lst)):
        money_total += species_quantity[i] * species_lst[i]
    give_back = float(input())                          # 表示要找零的金额
    if give_back > money_total:
        print("输入数据有误")
        return
    # 要想使用的钱币数量最少，那么就需要利用所有面值大的钱币，因此从数组的面值大的元素开始遍历，贪心算法开始
    i = 7
    while i >= 0:
        if give_back >= species_lst[i]:       # 要找零的金额大于等于找回钱币的面额时进行找零
            n = int(give_back/species_lst[i])   # 表示要找回金额的张数
            if species_quantity[i] >= n:        # 要找回的张数够
                species_quantity[i] -= n
                back_quantity[i] += n
                give_back -= n*species_lst[i]     # 金额动态改变（贪心的关键）
            else:
                back_quantity[i] = species_quantity[i]
                give_back -= species_quantity[i]*species_lst[i]
                species_quantity[i] = 0
            if give_back == 0:
                break
        i -= 1
    print(back_quantity)


change()
