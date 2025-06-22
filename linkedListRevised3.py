class Node :
    self.val = val
    self.next = next


class linkList :
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        head = node
    
    def insert_at_end(self,data):


        if self.head is None :
            self.insert_at_begining(data)
            return
        
        itr = self.head

        while itr:
            itr= itr.next
        
        node = Node(data, None)

        itr.next = node
    
    def insert_values(self,data_list):

        for data in data_list:
            self.insert_at_end(data)