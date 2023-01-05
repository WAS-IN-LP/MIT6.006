class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node1 = Doubly_Linked_List_Node(x)
        node2 = self.head
        
        # 链表不为空
        if node2:
            node1.next = node2
            node2.prev = node1
            self.head = node1
        # 链表为空
        else:
            self.head = node1
            self.tail = node1
        

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node1 = Doubly_Linked_List_Node(x)
        node2 = self.tail
        
        # 链表不为空
        if node2:
            node2.next = node1
            node1.prev = node2
            self.tail = node1
        # 链表为空    
        else:
            self.head = node1
            self.tail = node1

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = self.head
        
        # 链表不为空
        if node:
            x = node.item
            # 链表不仅只有1个节点
            if node.next:
                self.head = node.next
                node.next.prev = None
                node.next = None
             # 链表只有1个节点    
            else:
                self.head = None
                self.tail = None
        # 链表为空 则返回空              

        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = self.tail
        # 链表不为空
        if node:
            x = node.item
            # 链表不仅只有1个节点
            if node.prev:
                self.tail = node.prev
                node.prev.next = None
                node.prev = None
            # 链表只有1个节点
            else:
                self.head = None
                self.tail = None
        # 链表为空 则返回空 
                               
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        # 链表self L1不为空
        if x1:
            L2.head = x1
            # L1不仅只有一个节点
            if x2:
                L2.tail = x2
                # x1不是头结点
                if x1.prev:   
                    x1.prev.next = x2.next
                    # x2不是尾节点
                    if x2.next:                                
                        x2.next.prev = x1.prev
                        x1.prev = None
                        x2.next = None
                    # x2是尾节点
                    else:   
                        self.tail = x1.prev  
                        x1.prev = None                        
                        
                # x1是头结点
                else:
                    # x2不是尾节点
                    if x2.next:
                        self.head = x2.next
                        x2.next.prev = None
                        x2.next = None
                    # x2是尾节点
                    else:
                        self.head = None
                        self.tail = None
            # L1只有一个节点x1，没有节点x2
            else:
                L2.tail = x1
                self.head = None
                self.tail = None
        # 链表self L1为空,就什么也没有
        
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        # L2不为空
        if L2.head:
            # L1为空
            if x is None:
                self.head = L2.head
                self.tail = L2.tail
                L2.head = None
                L2.tail = None
            # L1不为空
            else:
                # L1只有一个节点x
                if x.next is None:
                    self.tail = L2.tail
                    L2.head.prev = x
                    x.next = L2.head
                    L2.head = None
                    L2.tail = None
                # L1不止一个节点
                else:
                    L2.head.prev = x
                    L2.tail.next = x.next
                    x.next.prev = L2.tail
                    x.next = L2.head
                    L2.head = None
                    L2.tail = None
                    
                    
            
 