class Node :
    def __init__(self):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,none)
        self.head = node
    
    def insert_at_end(self,data):

        if self.head == None :
            insert_at_begining(self,data)
            return
        
    
        itr= self.head

        while itr.next:

            itr = itr.next
        
        node = Node(data,none)

        itr.next = node

    def insert_values(self,data_list):

        for data in data_list:
            insert_at_end(data)

    def get_length(self):

        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at(self,data,index):

        if index < 0 or index > self.get_length() :
            raise Exception("Invalid Index")
        
        if index == 0 :
            insert_at_begining(data)
        
        itr = self.head
        count = 0

        while itr :
            
            if count == index-1 :
                node = Node(data,none)
                itr.next = node

            itr = itr.next
            count = count + 1

    def remove_at(self,index):
        if index < 0 or index >= self.get_length() :
            raise Exception("Invalid Index")
        
        if index == 0 :

            self.head = self.head.next
            return


            itr = self.head
            count = 0

            while itr :
                
                if (count ==  index -1):
                    itr = itr.next.next
                    break

                itr = itr.next
                count +=1


