class Node:
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name 要以 / 结尾
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    # 展示当前目录下的所有子文件
    def ls(self):
        return self.now.children

    # 切换目录
    def cd(self, name):
        if name[-1] != "/":
            name+="/"
        # 如果输入的是  .. 那么路径会向上一层
        if name == "../":
            self.now=self.now.parent
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        # 要是找不到引发一个报错
        raise ValueError("没有这一个文件夹")


tree = FileSystemTree()
"""--------------------------测试数据--------------"""
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("user/")
tree.cd("bin/")
tree.mkdir("python/")
print(tree.ls())