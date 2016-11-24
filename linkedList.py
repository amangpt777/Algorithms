class Node :
    
    def __init__(self, data = None, next_node = None) :
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList :
    
    def __init__(self, head = None) :
        self.head = head
        
    def insert(self, data) :
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, data) :
        node = self.head
        while node.get_next() != None :
            if node.get_data() == data :
                break
            node = node.get_next()
        if node.get_data() == data :
            return node
        else :
            return None
        

lList = LinkedList()
lList.insert(2)
lList.insert(4)
node = lList.search(4)
print(node.get_data())
