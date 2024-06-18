"""列表获取单个元素"""
"""
1.正向索引从0到n-1
2.逆向索引从-1到-n
3.指定索引不存在，输出ValueError
"""

"创建一个列表"
lst = ["hello", "world", "hello", 23, "52"]
"打印索引为3的元素"
print(lst[3])
"打印索引为-4的元素"
print(lst[-2])
"""打印索引为10的元素
print(lst[10])
报错因为不存在 IndexError: list index out of range
"""