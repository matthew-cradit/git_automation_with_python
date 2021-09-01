class Node:
    def __init__(self, val):
        self.left = None 
        self.right = None
        self.value = val
    
    def insert(self,val):
        if val < self.value:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        elif val > self.value:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)

#function for finding center of list
def center(s_list):
    return len(s_list) // 2

class Tree:

    def __init__(self):
        self.root = None
        
    def create_tree(self, s_list):
        val = center(s_list)
        if self.root:
            self.root.insert(s_list[val])
        else:
            self.root = Node(s_list[val])

        if len(s_list) == 1:
            return
        else:
            self.create_tree(s_list[:val])
            
            if len(s_list) > 2:
                self.create_tree(s_list[val+1 :])
        
    def print_t(self, node = None):
        
        if node == None:
            node = self.root
        
        if node.left:
            self.print_t(node.left)
            print(node.value)
            if node.right:
                self.print_t(node.right)
        else:
            print(node.value)

            
        
if __name__ == '__main__':
    list_one = [1 ,2 ,3,4,5,6,7]
    list_two = [10, 20, 30, 40 ]
    list_three = [3, 40, 500, 6000, 70000]
    list_four = [65, 38, 197,1, 5]
    t1 = Tree()
    t2 = Tree()
    t3 = Tree()
    t4 = Tree()
    t1.create_tree(list_one)
    t2.create_tree(list_two)
    t3.create_tree(list_three)
    t4.create_tree(sorted(list_four))
    print("tree 1")
    t1.print_t()
    print("tree 2")
    t2.print_t()
    print("tree 3")
    t3.print_t()
    print('tree 4')
    t4.print_t()

