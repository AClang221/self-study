"""
str.lower():将str字符串全部转成小写字母，结果为一个新的字符串

str.upper()：将str字符串全部转成大写字母，结果为一个新的字符串

str.split(sep=值)

str.count(值)：结果为（值）在列表中出现的次数

str.find(值)：查询（值）在字符串中是否存在，如果不存在结果为-1，存在结果为（值）首次出现的索引

str.index(值)：功能与find相同，区别在不存在时程序报错

str.startswith(值)：查询字符串是否以（值）开头

str.endswith(值)：查询字符串是否以（值）结尾

str.replace(old,news,nub):使用news替换字符串中所有的old字符串，nub表示的是替换的次数，结果是一个新的字符串

str.center(width,fillchar):字符串在指定的范围内居中，可以使用fillchar进行填充

str.strip():去除字符串左右的指定字符，不写默认为去空格，但是中间的不能去，如果写了参数，请看下列示例
str.lstrip():同上，去除左侧字符
str.rstrip():去除右侧字符


str.join(iter):在iter中的每个元素的后面都增加一个新的字符串
"""
a="abbbaacdef"
b="lad_adawasdad_adl"
print(a.split(sep="a"))
print(a.count("a"))
print(a.startswith("a"))
print(a.replace("a","m",1))
print(a.center(20,"*"))
print(b.strip("dal"))


