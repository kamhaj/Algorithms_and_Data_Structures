'''
There are some issues with array (list) that linked list tries to solve.

If we use linkes (like *) in each element to point to the next one,
instead of coping/shifting elements on deletion/insertion, we just need to
change a reference (but we do not have indexing, so we need to iterate to this element).
We also do not have to preallocate any memory like in arrays (lists).

                                            Array               Linked List
                            indexing         O(1)                   O(n)                
insert/delete elem. at the beginning         O(n)                   O(1)
      insert/delete elem. at the end         O(1) - amortized*      O(n) 
        insert element in the middle         O(n)                   O(n)


*amortized means that additionally, we have to allocate more memory if no left

## insert/delete element at the end BigO(n) -- why? because you have to iterate to this elements

'''



class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None: # linked list is blank
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:     # while iteration is None, it is a last element
            itr = itr.next

        ## insert new element
        itr.next = Node(data, None)

    ## create a NEW linked list based on values provided in an array
    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    ## insert element at index (starts with 0)
    def insert_at(self, idx, data):
        ## validate index
        if idx<0 or idx>=self.get_length():
            raise ValueError('Invalid index.')

        ## check if head
        elif idx==0:
            self.insert_at_beginning(data)
            return
        
        else:
            count = 0
            itr = self.head
            while itr:
                # stop at previous element
                if count == idx - 1:
                    itr.next = Node(data=data, next=itr.next)
                    break
                itr = itr.next
                count+=1

    ## remove element at index (starts with 0)
    def remove_at(self, idx):
        ## validate index
        if idx<0 or idx>=self.get_length():
            raise ValueError('Invalid index.')
        
        ## check if head
        elif idx==0:
            self.head = self.head.next
            return
        
        else:
            count = 0
            itr = self.head
            while itr:
                # stop at previous element
                if count == idx - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count+=1


    ## get linked list length
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr=itr.next
            count += 1
        return count

    ## print linked list
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        linked_list_string = '\n'
        # iterate through elements
        while itr:
            linked_list_string += str(itr.data) + ' --> '
            itr = itr.next
        print(linked_list_string[:len(linked_list_string)-len(' --> ')])


if __name__ == '__main__':
    ## create linked list and insert some nodes
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(8)    
    ll.insert_at_beginning(14)
    ll.insert_at_end(123)

    ## print linked list and get its length
    ll.print()
    print(f'Above linked list length is {ll.get_length()}')


    ## create a new linked list using one command
    ll2 = LinkedList()
    ll2.insert_values(['apples', 'carrots', 'pees', 'grapes', 'bananas', 'plums', 'pears'])

    ## remove values by indices
    ll2.remove_at(idx=0)        # apples
    ll2.remove_at(idx=2)        # grapes
    ll2.insert_at(idx=3, data='peaches')        # bananas --> peaches --> plums
    ll2.insert_at(idx=0, data='dragon fruit')

    ## print linked list and get its length
    ll2.print()
    print(f'Above linked list length is {ll2.get_length()}')
