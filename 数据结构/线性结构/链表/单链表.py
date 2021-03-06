
## 节点创建类
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

    def get_element(self):
        return self.element
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


## 链表类
class Linklist:

    # 初始化：只有头节点 data=None,next=None
    def __init__(self, element):
        self.head = Node(element)
        self.size = 0


    # 尾部插入
    def append(self, data):
        new_node = Node(data)  # 指向None
        # 遍历到尾部节点
        p = self.head
        while p.next != None:
            p = p.next
        p.next = new_node

        self.size += 1


    # 头部插入
    def add(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        self.size += 1


    # 插入第idx个节点
    def insert(self, data, idx):
        new_node = Node(data)
        
        if idx == 0:
            raise Exception('can not insert,as 0 index is head') # 第0个是头节点
        else:
            p = self.head
            while idx - 1:  # 遍历到前一个节点
                p = p.next
                if p == None:
                    raise Exception('out of range')  # 尾节点有数据
                idx -= 1

            new_node.next = p.next # 此时 p.next 指向第index个节店
            p.next = new_node

            self.size += 1            
    

    # 删除第idx个节点: O(n)
    def remove_by_idx(self, idx):
        
        if idx == 0:
            raise Exception('can not remove,as 0 index is head') # 第0个是头节点
        if idx > self.size or idx < 0:
            raise Exception('out of range')
        else:
            p = self.head
            while idx - 1:  # 遍历到前一个节点 
                p = p.next
                idx -= 1

            p.next = p.next.next # 前一个指针直接跨越过去

            self.size -= 1  

    


    # 获取第idx节点数据
    def get_element(self, idx):

        if idx == 0:
            return None # 头节点
        if idx > self.size or idx < 0:
            raise Exception('out of range')
        else:
            p = self.head
            while idx:
                p = p.next
                idx -= 1
            
            return p.element


    # 查询元素是否在链表
    def get_index(self, data):
        p = self.head
        for i in range(self.size + 1):
            if p.element == data:
                return i
            p = p.next
        
        print('can not find')

    # 遍历链表并存储在数组
    def traverse(self):
        elems = []
        p = self.head

        while p != None: 
            elems.append(p.element)
            p = p.next   
        print(elems)

    # 反转打印链表
    def reverse(self):
        elem = []
        p = self.head.next
        while p != None:
            elem.insert(0, p.element)
            p = p.next
        print(elem)


    # 判断链表是否为空
    def is_empty(self):
        return self.size == 0
    
    # 统计链表长度
    def get_length(self):
        return self.size
    
    
    

if __name__ == "__main__":
    l = Linklist(10)
    l.append(10)
    l.add(1)
    l.add(2)
    l.add(3)
    l.reverse()
    l.traverse()
   
    
    


