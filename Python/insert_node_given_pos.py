'''
    {
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
def addElement(head, M, K):
    new_node = Node(K)

    if M==1:
        new_node.next = head
        return new_node
    
    current = head
    for _ in range(M-2):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return head
