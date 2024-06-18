itea = ["zhang", "lin", "wu"]  # 新建一个键

prices = [60, 80, 100]  # 新建一个值

d = {itea.upper(): prices for itea, prices in zip(itea, prices)}  # zip函数完成字典生成，upper让键变为大写字母
print(d)

itn = ["zhang", "zhe"]
print("如果键与值的数量对不上，默认按照短的进行排列")
a = {itn.upper(): prices for itn, prices in zip(itn, prices)}  # zip函数完成字典生成，upper让键变为大写字母
print(a)
